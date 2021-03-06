from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.

class Seller(models.Model):
	title = models.CharField('Продавец', max_length=150, unique=True)
	email = models.EmailField('email', blank=True, unique= True )

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

	def get_delete_url(self):
		return reverse('category_delete_url', kwargs={'pk':self.pk})



class Item(models.Model):
	title = models.CharField('Название', max_length=150, db_index=True)
	description = models.TextField(blank=True,db_index=True)
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, null=True)
	price = models.IntegerField('Цена товара', blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	adress = models.CharField('Адрес', max_length = 250)
	date_pub = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Владелец', blank=True)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('item_detail_url', kwargs = {'pk': self.pk})

	def get_delete_url(self):
		return reverse('item_delete_url', kwargs = {'pk': self.pk})

	def get_update_url(self):
		return reverse('item_update_url', kwargs = {'pk': self.pk})



class ProductPhoto(models.Model):
	photo = models.ImageField(upload_to='item_photo/',verbose_name='Image')
	product = models.ForeignKey(Item, on_delete=models.CASCADE)
	


