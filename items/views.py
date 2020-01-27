from django.shortcuts import render, redirect
from .models import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm, ItemForm, PhotoForm,PhotoFormSet, PhotoInlineFormSet, AuthUserForm, RegisterUserForm		
from django.shortcuts import redirect
import datetime
from django.core.files.base import ContentFile
from django.forms import modelformset_factory
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CategoryList(ListView):
	'''list of categories'''
	model = Category


class CategoryDetail(View):
	'''description category'''
	def get(self, request, pk):
		model = Category.objects.get(id=pk)

		data = model.item_set.all()
		return render(request, 'items/category_detail.html', context = {'data' : data, 'category': model})

class ItemList(ListView):
	'''list of items'''
	model = Item
	queryset = Item.objects.order_by('-date_pub')

class ItemDetail(DetailView):
	'''description item'''
	model = Item
	

class SellerList(ListView):
	'''list of sellers'''
	model = Seller

class SellerDetail(DetailView):
	'''description seller'''
	model = Seller

#class AddCategory(FormView):
#    form_class = CategoryForm
#    template_name = 'items/add_category.html'

class AddCategory(View):
	def get(self, request):
		form = CategoryForm()
		return render(request, 'items/add_category.html', context={'form': form})

	def post(self, request):
		cat = CategoryForm(request.POST)

		if cat.is_valid(): #проверяем валидность данных
			new_cat = cat.save()
			print(new_cat.id)
			return redirect(new_cat) # отправляем на страницу с категорией	
		return render(request, 'items/add_category.html', context={'form' : cat })


class AddItem(LoginRequiredMixin, View):
	login_url = reverse_lazy('login_user_url')

	def get(self, request):
		new_item = ItemForm()
		formset = PhotoFormSet(queryset=ProductPhoto.objects.none())
		return render(request, 'items/add_many_image_item.html', context = {'new_item': new_item, 'formset': formset })

	'''
	def post(self, request):
		its = ItemForm(request.POST)
		image = PhotoForm(request.POST, request.FILES)
		if its.is_valid() and image.is_valid():
			new_item = its.save(commit=False)
			new_item.date_pub=datetime.datetime.now()
			new_item.save()
			for f in request.FILES.getlist('photo'):
				data = f.read()
				photo = ProductPhoto(product = new_item)
				photo.photo.save(f.name, ContentFile(data))
				photo.save()

			return redirect(new_item)
		print(image.errors)
		return render(request, 'items/add_item.html', context = {'form': its, 'image': image})
		'''

	def post(self, request):
		
		new_item = ItemForm(request.POST)
		formset = PhotoFormSet(request.POST, request.FILES, queryset=ProductPhoto.objects.none())
		if new_item.is_valid() and formset.is_valid():
			item = new_item.save(commit=False)
			item.user = request.user
			item.save()

			for form in formset.cleaned_data:
				#this helps to not crash if the user   
				#do not upload all the photos
				if form:
					image = form['photo']
					photo = ProductPhoto(product=item, photo=image)
					photo.save()
				messages.success(request,
                             "Yeeew, check it out on the home page!")
			return redirect(item)
		else:
			print(new_item.errors, formset.errors)
			return render(request, 'items/add_many_image_item.html', context = {'new_item': new_item, 'formset': formset})

class CategoryUpdate(View):
	def get(self, request, pk):
		category = Category.objects.get(id = pk)
		category_form = CategoryForm(instance=category)
		return render(request, 'items/category_update_form.html', context={'form': category_form, 'category': category })
	
	def post(self, request, pk):
		category = Category.objects.get(id=pk)
		cat_form = CategoryForm(request.POST, instance=category)

		if cat_form.is_valid():
			new_cat = cat_form.save()
			return redirect(new_cat)
		return render(request, 'items/category_update_form.html', context={'form': cat_form, 'category': category })

class ItemUpdate(LoginRequiredMixin, View):

	def get(self, request, pk):
		item = Item.objects.get(id=pk)
		new_item = ItemForm(instance=item)
		image = ProductPhoto.objects.filter(product = item)
		formset = PhotoInlineFormSet(instance = image)
		return render(request, 'items/update_item.html', context = {'new_item': new_item, 'formset': formset, 'item': item })




	def post(self, request, pk):
		item = Item.objects.get(id=pk)
		new_item = ItemForm(instance = item)
		formset = PhotoInlineFormSet(request.POST, request.FILES, instance=item)

		if new_item.is_valid() and formset.is_valid():
			item = new_item.save(commit=False)
			#item.user = request.user
			item.save()
			formset.save()
			#for form in formset.cleaned_data:
			#	#this helps to not crash if the user   
			#	#do not upload all the photos
			#	if form:
			#		image = form['photo']
			#		photo = ProductPhoto(product=item, photo=image)
			#		photo.save()
			#	messages.success(request,
            #                 "Yeeew, check it out on the home page!")
			return redirect(item)
		else:
			print(new_item.errors, formset.errors)
			return render(request, 'items/update_item.html', context = {'new_item': new_item, 'formset': formset})


class CategoryDelete(LoginRequiredMixin, View):
	def get(self,request, pk):
		cat = Category.objects.get(id=pk)
		return render(request, 'items/category_delete.html', context = {'category': cat})

	def post(self, request, pk):
		cat = Category.objects.get(id=pk)
		cat.delete()
		return redirect(reverse('category_list_url'))


class ItemDelete(LoginRequiredMixin, View):
	def get(self,request, pk):
		item = Item.objects.get(id=pk)
		return render(request, 'items/item_delete.html', context = {'item': item})

	def post(self, request, pk):
		item = Item.objects.get(id=pk)
		item.delete()
		return redirect(reverse('item_list_url'))

#Authorization

class LoginUserView(LoginView):
	template_name = 'items/login.html'
	form_class = AuthUserForm
	success_url = reverse_lazy('item_list_url')
	def get_success_url(self):
		return self.success_url


#Register
class RegisterUserView(CreateView):
	model = User
	template_name = 'items/register.html'
	form_class	= RegisterUserForm	
	success_url	= reverse_lazy('item_list_url')
	success_msg = 'Пользователь зарегистрирован'

	def form_valid(self, form):
		form_valid = super().form_valid(form)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		auth_user = authenticate(username = username, password = password)
		login(self.request, auth_user)
		return form_valid

class UserLogout(LogoutView):
	next_page = reverse_lazy('item_list_url')

