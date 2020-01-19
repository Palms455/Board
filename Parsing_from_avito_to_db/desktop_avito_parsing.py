import requests
from bs4 import BeautifulSoup


'''
Парсинг десктопной версии 
Заголовок, цена, описание, адрес, фото, номер объявления

'''



class Article():

	def __init__(self, url):
		self.url = url
		self.get_html()
		self.data

	def get_html(self):

		r = requests.get(self.url)
		self.get_page_data(r.text)
		

	def get_file(self, url):
		r = requests.get(url)
		return r.content

	def get_page_data(self, html):
		soup = BeautifulSoup(html, 'lxml')
		
		title = soup.find('span', class_="title-info-title-text").text
		print(title)
		
		try:
			adress = soup.find('span', class_="item-address__string").text
			
		except:
			adress=''
		try:
			price = soup.find('span', class_='js-item-price').text
			
		except:
			price = ''
		category = soup.find('div', class_='breadcrumbs').find('meta', content='4').find_previous_sibling().get('title')
		try:
			description = soup.find('div', class_='item-description-text').text.strip()
			
		except:
			description = ''
		seller = soup.find('div', class_='seller-info-name js-seller-info-name').find('a').text
		item_id = soup.find('span', {'data-marker' : 'item-view/item-id'}).text.split()[1]
		print(item_id)

		try:
		
			images_urls = soup.find_all('div', class_='gallery-img-wrapper js-gallery-img-wrapper')
			
			image=[]
			for i in images_urls:
				
				image_url = 'https:' + i.find('div', class_='gallery-img-frame').get('data-url')
				image.append(self.get_file(image_url))
		except:
			image = ''

		self.data = {'adress': str(adress), 'price': str(price), 'title': str(title), 'category': str(category), 'description': str(description), 'item_id': str(item_id), 'image': image, 'seller': seller}
		return self.data


		

def main():
	url = 'https://www.avito.ru/samara/igry_pristavki_i_programmy/nintendo_wii_2008_goda_c_hraneniya_1809071245?slocation=621540'
	p = Article(url)
	i = 0
	
	db.connect()
	db.create_tables([Product, ProductFoto, Seller ])
	try:
		owner = Seller.get(seller = p.data['seller'])
	except DoesNotExist:
		Seller.create(seller = p.data['seller'])

	Product.create(title=p.data['title'], price=p.data['price'], adress= p.data['adress'], description=p.data['description'], category = p.data['category'], seller=p.data['seller'], item_id=p.data['item_id'])
	for imagin in (p.data['image']):
		file=open(f'{i}.jpg', 'wb')
		file.write(imagin)
		file.close()
		i +=1
		ProductFoto.create(image = imagin, item_id = p.data['item_id'])
	for item in Product.select():
		print(item.seller.seller,'\n', item.title, item.price, item.description)

if __name__ == '__main__':
	main()