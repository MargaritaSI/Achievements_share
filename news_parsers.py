import requests

from bs4 import BeautifulSoup
from datetime import datetime
from webapp import create_app
from webapp.db import db
from webapp.news.models import News


def get_articles_by_tag(url, tag="productivity"):
    try:
        url = url + tag
        result = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        result.raise_for_status()

        articles = []
        if result.text:
            soup = BeautifulSoup(result.text, 'html.parser')
            if 'hays.com' in url:
                articles = parse_hays_article(soup)
            if 'theladders.com' in url:
                articles = parse_ladders_article(soup)
            if 'medium.com' in url:
                articles = parse_medium_article(soup)
        return articles

    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def parse_hays_article(soup):
    articles = []
    all_articles = soup.findAll('a', class_="boxlink")
    for article in all_articles:
        title = article['data-title']
        url = article['href']
        articles.append(("Hays", title, url))
    return articles


def parse_ladders_article(soup):
    articles = []
    all_articles = soup.findAll('div', class_="article-title-container")
    for article in all_articles:
        title = article.find('h3', class_="article-title").text
        url = article.find('a')['href']
        url = f"https://www.theladders.com{url}"
        articles.append(("Ladders", title, url))
    return articles


def parse_medium_article(soup):
    articles = []
    all_articles = soup.find('div').findAll('article')
    for article in all_articles:
        title = article.find('h2').text
        article_attrs = {"aria-label": "Post Preview Image"}
        url = article.find('a', attrs=article_attrs)
        if url == None:
            continue
        url = f"https://medium.com{url['href'].split('?')[0]}"
        articles.append(("Medium", title, url))
    return articles


def save_news(source, title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_news = News(
            title=title, url=url, published=published, source=source
        )
        db.session.add(news_news)
        db.session.commit()


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        medium_articles = get_articles_by_tag(
            "https://medium.com/tag/",
            "life-lessons"
        )

        for article in medium_articles:
            save_news(*(article + (datetime.now(),)))
