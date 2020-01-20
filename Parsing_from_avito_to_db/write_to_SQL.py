
from peewee import *
from desktop_avito_parsing import Article
from simple_avito_to_sql import get_html, get_site_list
from random import randint
import time
import datetime



db = PostgresqlDatabase(database='django_db', user='rustam', password='3301344', host='localhost')


class BaseModel(Model):
    class Meta:
        database = db

class Items_Seller(BaseModel):
	title = CharField( unique=True)

	

class Items_Category(BaseModel):
	title = CharField( unique=True)
	

class Items_Item(BaseModel):
	title = CharField()
	description = TextField()
	seller = ForeignKeyField(Items_Seller)
	price = CharField()
	category = ForeignKeyField(Items_Category)
	adress = CharField()
	date_pub = DateTimeField()





class Items_ProductPhoto(BaseModel):
	photo = CharField()
	product = ForeignKeyField(Items_Item)
	
	
def main():
	db.connect()
	db.create_tables([Items_Item, Items_ProductPhoto, Items_Seller, Items_Category, ])
	print('connect to db')
	site_list_all=[]
	url = 'https://www.avito.ru/rossiya?q=nintendo+wii&p=1'
	for k in range(1, 5):
		urls = f'https://www.avito.ru/rossiya?q=nintendo+wii&p={str(k)}'
		time.sleep(randint(3,8))
		site_list=(get_site_list(get_html(urls)))
		for site in site_list:
			site_list_all.append(site)
	j=0
	print('now, we get site list')
	for site in  site_list_all:
		print(site)
		time.sleep(randint(4, 10))
		p = Article(site)
		try:
			owner = Items_Seller.get(title = p.data['seller'])
		except DoesNotExist:
			owner = Items_Seller.create(title = p.data['seller'])
		try:
			categories = Items_Category.get(title = p.data['category'])
		except DoesNotExist:
			categories = Items_Category.create(title = p.data['category'])

		
		q = Items_Item.create(title=p.data['title'], price=p.data['price'], adress= p.data['adress'], description=p.data['description'], category = categories, seller=owner, date_pub=datetime.datetime.now())
		i = 0 
		for imagin in (p.data['image']):
			file=open(f'media/item_photo/{j}_{i}.jpg', 'wb')
			file.write(imagin)
			file.close()
			Items_ProductPhoto.create(photo = f'{j}_{i}.jpg', product = q.id)
			i +=1
		j +=1



if __name__ == '__main__':
	main()