from django.shortcuts import render, redirect
#from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from .forms import SearchForm
from django.contrib import messages
import requests

def index(request):
	form = SearchForm()
	result_titles = []
	result_links = []
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			query = request.POST.get('search')
			query = query.replace(' ', '+')
			url = str('https://stackoverflow.com/search?q=' + query)
			query = query.replace('+', ' ')

			#new
			headers = {
			    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
			    'Content-Type': 'text/html',}

			response = requests.get(url, headers=headers)
			page_html = response.text
			page_soup = soup(page_html, 'html.parser')

			title = page_soup.find("meta", property="og:url")
			print(title['content'])

			#data = page_soup.find_all('a', {'question-hyperlink'})
			"""for a in data:
				result_links.append(str('https://stackoverflow.com' + (a['href'])))
			for t in data:
				link = t.text
				result_titles.append(link)
			result_titles = result_titles[:15]
			result_links = result_links[:15]
			new_list = zip(result_titles, result_links)

			context = {
				'query': query,
				'new_list': new_list,
				'form': form}
			return render(request, 'results.html', context)"""

		else:
			form = SearchForm()
	return render(request, 'results.html', {'form': form})



