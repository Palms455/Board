from selenium import webdriver
import os
import time
'''
используем   - это headless webkit браузер для селениум
update - отложено. надо разобраться как заходить на мобильную версию
'''


class Driver():
	def __init__(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		self.browser = webdriver.Chrome()#chrome_options=options)
		
		self.number = None

	def navigate(self, url):
		self.browser.set_window_size(450, 300)
		self.browser.get(url)
		ActionChains(browser).key_down(Keys.LEFT_CONTROL).key_down(Keys.LEFT_SHIFT).send_keys('i').perform()
		self.browser.get(url)
		self.browser.implicitly_wait(5)
		self.browser.find_element_by_class_name('BPWk2').click()
		self.number = self.browser.find_element_by_class_name('_3Ryy-').text
		return self.number



def main():
	pass



if __name__ == '__main__':
	main()

