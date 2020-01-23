from django.shortcuts import render, redirect
from .models import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, FormView
from .forms import CategoryForm, ItemForm, PhotoForm,PhotoFormSet
from django.shortcuts import redirect
import datetime
from django.core.files.base import ContentFile
from django.forms import modelformset_factory
from django.contrib import messages


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

class AddItem(View):

	def get(self, request):
		new_item = ItemForm()
		formset = PhotoFormSet(queryset=ProductPhoto.objects.none())
		return render(request, 'items/add_many_img_item.html', context = {'new_item': new_item, 'formset': formset })

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
			#item.user = request.user
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
		

class ItemUpdate(View):
	pass


