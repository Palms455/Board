from django.shortcuts import render, redirect
from .models import Item, Category, Seller
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

# Create your views here.
class CategoryList(ListView):
	'''list of categories'''
	model = Category

class CategoryDetail(DetailView):
	'''description category'''
	model = Category
	query_set = Category.objects.all

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

