from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Seller(models.Model):
	title = models.CharField('Продавец', max_length=150, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('seller_detail_url', kwargs={'pk': self.pk})

class Category(models.Model):
	title = models.CharField('Категория', max_length= 150, unique=True)
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category_detail_url', kwargs={'pk':self.pk})

class Item(models.Model):
	title = models.CharField('Название', max_length=150)
	description = models.TextField(blank=True)
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
	price = models.IntegerField('Цена товара', blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	adress = models.CharField('Адрес', max_length = 250)
	date_pub = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('item_detail_url', kwargs = {'pk': self.pk})



class ProductPhoto(models.Model):
	photo = models.ImageField(upload_to='item_photo/')
	product = models.ForeignKey(Item, on_delete=models.CASCADE)
	


