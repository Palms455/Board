from django.shortcuts import render, redirect
from .models import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import CategoryForm, ItemForm, PhotoForm
from django.shortcuts import redirect


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
		photo = PhotoForm()
		return render(request, 'items/add_item.html', context = {'form': form, 'photo': photo})

	def post(self, request):
		item = ItemForm(request.POST)
		photo = PhotoForm(request.POST)
		if item.is_valid():
			new_item = item.save()
			new_photo = photo.save(new_item.id)
			return redirect(new_item)
		return render(request, 'items/add_item.html', context = {'form': item, 'photo': photo})