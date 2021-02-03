import requests

import config

from bs4 import BeautifulSoup

def parse_clients():
	url = 'https://doka-it.ru/proektyi/?project_category=all'
	HEADERS = {
		'User-Agent': config.User_Agent
	}
	mass=''
	responce = requests.get(url, headers= HEADERS)
	soup = BeautifulSoup(responce.content, 'html.parser')
	items = soup.findAll('div', class_='clients__item-item wow fadeInLeft')
	news = []
	
	for item in items:
		try:
			news.append({
				'title': item.find('p', class_="title").get_text(strip=True),
				})
		except AttributeError:
				pass
	i=0
	while i<5: 
		mass+='• '+news[i]['title']+'\n'
		i+=1
	return mass

def parse_adres():
	url = 'https://doka-it.ru/kontaktyi//'
	HEADERS = {
		'User-Agent': config.User_Agent
	}
	mass=''
	responce = requests.get(url, headers= HEADERS)
	soup = BeautifulSoup(responce.content, 'html.parser')
	items = soup.findAll('div', class_='contacts_wrap col-lg-6')
	adres = []
	
	for item in items:
		try:
			adres.append({
						'title': item.find('p', class_="contact-item__title").get_text(strip=True),
						'adr' : item.find('div', class_="contact-item").get_text(strip=True),
				})
		except AttributeError:
			pass

	for i in adres: 
		mass+=i['title']+':\n'+i['adr']+'\n\n'
	return(mass)


