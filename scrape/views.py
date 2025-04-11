from django.shortcuts import render
from bs4 import BeautifulSoup as soup 
import requests
import re

def index(request):
    posts_num = 4
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html',
    }

    posts = []

    # The Verge
    response = requests.get('https://www.theverge.com/', headers=headers)
    verge_soup = soup(response.text, 'html.parser')
    verge_articles = verge_soup.find_all('div', "c-entry-box--compact__body")
    verge_authors = verge_soup.find_all('span', 'c-byline__author-name')
    verge_images = verge_soup.find_all('img')

    for i in range(posts_num):
        posts.append({
            'title': verge_articles[i].a.text,
            'url': verge_articles[i].a.get('href'),
            'image': verge_images[i].get('src'),
            'author': verge_authors[i].text,
            'source_name': 'theverge.com',
            'source_url': 'https://www.theverge.com/'
        })

    # TechCrunch
    response = requests.get('https://techcrunch.com/', headers=headers)
    crunch_soup = soup(response.text, 'html.parser')
    crunch_articles = crunch_soup.find_all('a', "post-block__title__link")
    crunch_authors = crunch_soup.find_all('div', 'river-byline')
    crunch_images = crunch_soup.find_all('img')

    for i in range(posts_num):
        posts.append({
            'title': crunch_articles[i].text.strip(),
            'url': crunch_articles[i].get('href'),
            'image': crunch_images[i].get('src')[:-19],
            'author': crunch_authors[i].a.text.strip(),
            'source_name': 'techcrunch.com',
            'source_url': 'https://www.techcrunch.com/'
        })

    # Gizmodo
    response = requests.get('https://gizmodo.com/', headers=headers)
    giz_soup = soup(response.text, 'html.parser')
    giz_list = giz_soup.find_all('div', 'js_curation-block-list')
    giz_images = giz_soup.find_all('img')
    giz_authors = giz_list[0].find_all('a')
    giz_url = giz_authors[0].get('href')

    author_list = [
        giz_authors[3].text, giz_authors[15].text,
        giz_authors[19].text, giz_authors[7].text,
        giz_authors[11].text
    ]

    for i in range(posts_num):
        srcset = giz_images[i].get('srcset', '')
        image = re.split(', ', srcset)[i][:-5] if srcset else giz_images[i].get('src') # find highest quality image in srcset
        posts.append({
            'title': giz_images[i].get('alt', '')[17:],  # skip 'Image for article: '
            'url': giz_url,
            'image': image,
            'author': author_list[i],
            'source_name': 'gizmodo.com',
            'source_url': 'https://www.gizmodo.com/'
        })

    return render(request, 'index.html', {'posts': posts})
