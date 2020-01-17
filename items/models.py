from django.db import models

# Create your models here.
class Item(models.Model):
	title = models.CharField('Название', max_length=250)
	description = models.TextField(blank=true)
	number = models.CharField(max_length=15, blank=true)
	seller = models.ForeignKeyField(Seller, on_delete=models.CASCADE)
	price = models.IntegerField('Цена товара', blank=True)
	category_id = models.ForeignKeyField(Category, on_delete=models.CASCADE)
	photo = models.ManyToManyField(PProductPhoto, related_name=product_item)


class Seller(models.Model):
	title = models.CharField('Продавец', max_length=150, unique=True)


class Category(models.Model):
	title = models.CharField('Категория', unique=True)
	city_id = models.ForeignKeyField(City, on_delete=models.CASCADE)

class ProductPhoto(models.Model):
	photo = BlobField()
	

class City(modesls.Model):
	name = CharField(max_length=150, unique=True)
