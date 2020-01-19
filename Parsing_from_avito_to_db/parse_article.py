import requests
import csv
from bs4 import BeautifulSoup
'''
Парсинг объявления мобильной версии
to do : научииться вытаскиватб картинки
'''



class Article():

	def __init__(self, url):
		self.url = url
		self.get_html()
		self.image = []

	def get_html(self):
		user_agent = { 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}
		r = requests.get(self.url, headers = user_agent)
		self.get_page_data(r.text.encode('utf-8'))
		print(r.text)

	def get_page_data(self, html):
		soup = BeautifulSoup(html, 'lxml')
		print(soup)
		title = soup.find('h1', class_='_3Yuc4').find('span', class_='_12M45').text
		print(title)
		try:
			adress = soup.find('span', {'data-marker' : 'delivery/location'}).text
			print(adress)
		except:
			adress=''
		try:
			price = soup.find('span', {'data-marker': 'item-description/price'}).text
			print(price)
		except:
			price = ''
		category = soup.find('div', class_='_3JBAb').text
		try:
			description = soup.find('div', {'data-marker': 'item-description/text'}).text
			print(description)
		except:
			description = ''
		seller = soup.find('span', {'data-marker': 'seller-info/name'}).text
		
		images_urls = soup.find('img', class_='_-0hhG')
		print(images_urls)

			#print(images_urls)
			#for i in images_urls:
			#	image_url = i.soup.get('src')
			#	print(image_url)
			#	self.image.append(get_file(image_url))
			#	print(len(self.image))
		

		data = {'adress': adress, 'price': price, 'title': title, 'category': category, 'description': description}
		return data


def get_file(url):
	r = requests.get(url)
	return r.response



def main():
	url = 'https://m.avito.ru/moskva/igry_pristavki_i_programmy/nintendo_wii_tushka_1769950079'
	p = Article(url)
	for i in range(len(p.image)):
		file=open(f'{i}.jpg', 'wb')
		file.write(p.image[i])
		file.close()


if __name__ == '__main__':
	main()