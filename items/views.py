from django.shortcuts import render, redirect
from .models import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import CategoryForm, ItemForm, PhotoForm
from django.shortcuts import redirect
import datetime
from django.core.files.base import ContentFile


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

class ItemDetail(DetailView):
	'''description item'''
	model = Item
	

class SellerList(ListView):
	'''list of sellers'''
	model = Seller

class SellerDetail(DetailView):
	'''description seller'''
	model = Seller

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
		form = ItemForm()
		image = PhotoForm()
		return render(request, 'items/add_item.html', context = {'form': form, 'image': image })

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