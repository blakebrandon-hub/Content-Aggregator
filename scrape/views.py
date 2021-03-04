from django.shortcuts import render
from bs4 import BeautifulSoup as soup 
import requests
import re

def index(request):
	verge_urls = []
	verge_titles = []
	verge_authors = []
	verge_images = []
	crunch_urls = []
	crunch_titles = []
	crunch_authors = []
	crunch_images = []
	gizmodo_urls = []
	gizmodo_titles = []
	gizmodo_authors = []
	gizmodo_images = []
	posts_num = 5
	verge = 'https://www.theverge.com/'
	crunch = 'https://techcrunch.com/'
	gizmodo = 'https://gizmodo.com/'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
		'Content-Type': 'text/html',}
	#Collect and parse data from 'the verge'
	response = requests.get(verge, headers=headers)
	page_html = response.text
	verge_soup = soup(page_html, 'html.parser')
	verge = verge_soup.find_all('div', "c-entry-box--compact__body")
	verge_author = verge_soup.find_all('span', 'c-byline__author-name')
	verge_image = verge_soup.find_all('img')
	for i in range(posts_num):
		url = verge[i].a.get('href')
		title = verge[i].a.text
		author = verge_author[i].text
		image = verge_image[i].get('src')
		verge_urls.append(url)
		verge_titles.append(title)
		verge_authors.append(author)
		verge_images.append(image)
	#Collect and parse data from 'tech crunch'
	response = requests.get(crunch, headers=headers)
	page_html = response.text
	crunch_soup = soup(page_html, 'html.parser')
	crunch = crunch_soup.find_all('a', "post-block__title__link")
	crunch_author = crunch_soup.find_all('div', 'river-byline')
	crunch_image = crunch_soup.find_all('img')
	for i in range(posts_num):
		url = crunch[i].get('href')
		title = crunch[i].text.strip()
		author = crunch_author[i].a.text.strip()
		image = crunch_image[i].get('src')[:-19]
		crunch_titles.append(title)
		crunch_authors.append(author)
		crunch_images.append(image)
		crunch_urls.append(url)
	#collect are parse data from 'gizmodo'
	response = requests.get(gizmodo, headers=headers)
	page_html = response.text
	gizmodo_soup = soup(page_html, 'html.parser')
	gizmodo = gizmodo_soup.find_all('div', 'js_curation-block-list')
	gizmodo_image = gizmodo_soup.find_all('img')
	gizmodo_author = gizmodo[0].find_all('a')
	gizmodo_url = gizmodo_author[0].get('href')
	for i in range(posts_num):
		title = gizmodo_image[i].get('alt')
		title = title[17:]	
		images = gizmodo_image[i].get('srcset')
		images = re.split(" ", images)
		image = images[8]
		url = re.split(' ', gizmodo_url)
		gizmodo_urls.append(url[0])
		gizmodo_titles.append(title)
		gizmodo_images.append(image)		
		first_author = gizmodo_author[3].text
		second_author = gizmodo_author[15].text
		third_author = gizmodo_author[19].text
		fourth_author = gizmodo_author[7].text
		fifth_author= gizmodo_author[11].text
		gizmodo_authors.append(first_author)
		gizmodo_authors.append(second_author)
		gizmodo_authors.append(third_author)
		gizmodo_authors.append(fourth_author)
		gizmodo_authors.append(fifth_author)
	context = {
		'verge_titles': verge_titles,
		'verge_urls': verge_urls,
		'verge_images': verge_images,
		'verge_authors': verge_authors,
		'crunch_titles': crunch_titles,
		'crunch_urls': crunch_urls,
		'crunch_images': crunch_images,
		'crunch_authors': crunch_authors,
		'gizmodo_titles': gizmodo_titles,
		'gizmodo_urls': gizmodo_urls,
		'gizmodo_images': gizmodo_images,
		'gizmodo_authors': gizmodo_authors}
	return render(request, 'index.html', context)
