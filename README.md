# 📰 Content Aggregator

<img src='https://user-images.githubusercontent.com/50201165/113705217-03ea2400-9692-11eb-84b2-f04e8c759209.jpg' width='400' height='300'>

A Django-based web application that collects and displays articles from multiple sources. This project demonstrates web scraping, data aggregation, and clean presentation in a single-page web app.

## 🌟 Features

- Scrapes the latest articles from selected programming and tech news sites.
- Uses BeautifulSoup to parse HTML and extract titles and URLs.
- Displays all results on a single, clean dashboard.
- Built with Django for powerful backend capabilities and routing.
- Ready for deployment on platforms like Heroku.

## 🛠️ Tech Stack

- **Backend:** Django, Python
- **Scraping:** BeautifulSoup, Requests
- **Frontend:** HTML, CSS, Bootstrap

## 🧪 How It Works

1. Each scraper module targets a specific website.
2. Scraping functions retrieve and parse content using BeautifulSoup.
3. The data is rendered via Django views into dynamic templates.
4. The home page shows a list of recent articles from all sources.

## 🔧 Setup Instructions

### Clone the repository
git clone https://github.com/blakebrandon-hub/Content-Aggregator.git
cd Content-Aggregator

### Create and activate a virtual environment
Mac: python -m venv venv
source venv/bin/activate  
Windows: venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Run migrations
python manage.py migrate

### Start the development server
python manage.py runserver

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.

