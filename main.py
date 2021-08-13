import requests 
from bs4 import BeautifulSoup as BS




def get_html(url):
	#делаем запрос по адресу и получаем ответ 
	resp = requests.get(url)
	return resp.text


def get_soup(html):
	#получаем обьект bs4 в котором будем искать 
	soup = BS(html, 'lxml')
	return soup


def get_date(soup):
		#передаем вод html и название заголовок H3 и забираем текст
	
	date = soup.find('div', class_='row hidden-xs').find('h3').get_text()
	return date 





def get_titles(soup):
	items = soup.find('div', class_='col-xs-8').find_all('div', class_='show')#Находим нуждный div м забираем все div в которых лежат сериалы
	print(len(items))
	titles= []
	for item in items:
		#проходим циклом по всем библиотекам находим
		title = item.find('p', class_='show-title').get_text()
		print(title)
		titles.append(title)
	return titles

def main():
	url = 'https://www.ts.kg/'
	html = get_html(url) #Получаем исходный html страницы
	soup = get_soup(html) #Получаем обьект BS 
	date = get_date(soup) #Парсим дату со страницы 
	titles = get_titles(soup)# парсим название сериалов 
	print(date)
	print(*titles, sep='\n')

if __name__ == '__main__':
	main()