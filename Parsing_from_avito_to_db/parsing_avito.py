import requests
import csv
from bs4 import BeautifulSoup
from random import choice
import time



def get_html(url):
	#proxies = {'https': 'ipaddress: 5000'}
	p = get_proxy() #{'schema': '' , 'adress': ''}
	proxy = {p['schema']: p['adress']} # можно указать несколько прокси
	r = requests.get(url, proxies=proxy, timeout=5 )
	return r.text

def get_proxy():
	html = requests.get('https://free-proxy-list.net/').text
	proxies = []
	soup = BeautifulSoup(html, 'lxml')
	trs = soup.find('table', id= 'proxylisttable').find('tbody').find_all('tr')[:19]
	for tr in trs:
		tds = tr.find_all('td')
		adress = tds[0].text.strip()
		port = tds[1].text.strip()
		schema = 'https' if 'yes' in tds[6].text.strip() else 'http'
		proxy = {'schema': schema, 'adress': adress + ':' + port}

		proxies.append(proxy)
	return choice(proxies) #функция берет на вход список эелемнтов и возвращает рандомное значение из него



def get_page_number(url): 
	# found count pages
	r = get_html(url)
	soup = BeautifulSoup(r, 'lxml')
	page_count = soup.find('span', {"data-marker" : "pagination-button/next"}).find_previous_sibling('span').text
	return int(page_count)
	
def get_site_list(html):
	site_list = []
	soup = BeautifulSoup(html, 'lxml')
	items = soup.find_all('div', class_='snippet-horizontal')
	for i in items:
		url =  i.find('h3', class_='snippet-title').find('a', class_='snippet-link').get('href')
		print(url)
		site_list.append(url)
	return(site_list)


def main():
	url = 'https://www.avito.ru/rossiya?q=nintendo+wii&p=1'
	get_proxy()
	for i in range(2, (get_page_number(url) + 1)):
		urls = f'https://www.avito.ru/rossiya?q=nintendo+wii&p={str(i)}'
		time.sleep(2)
		print(urls)
		get_site_list(get_html(urls))



if __name__ == '__main__':
	main()