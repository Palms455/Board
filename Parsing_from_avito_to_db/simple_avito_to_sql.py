import requests
from bs4 import BeautifulSoup
import time

def get_html(url):
	r = requests.get(url)
	return r.text


def get_site_list(html):
	site_list = []
	soup = BeautifulSoup(html, 'lxml')
	items = soup.find_all('div', class_='snippet-horizontal')
	for i in items:
		url = 'http://www.avito.ru' + i.find('h3', class_='snippet-title').find('a', class_='snippet-link').get('href')
		site_list.append(url)
	return(site_list)



def main():
	url = 'https://www.avito.ru/rossiya?q=nintendo+wii&p=1'
	
	for i in range(2, 15):
		urls = f'https://www.avito.ru/rossiya?q=nintendo+wii&p={str(i)}'
		time.sleep(2)
		print(urls)
		get_site_list(get_html(urls))



if __name__ == '__main__':
	main()