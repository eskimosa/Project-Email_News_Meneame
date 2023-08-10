from bs4 import BeautifulSoup
import requests


def scrape_news():
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    html_text = requests.get('https://www.meneame.net/m/politica', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('div', class_='body horizontal')
    title_link = []
    for article in news[0:10]:
        published_date = article.find('span').text.replace('por', '')
        link = article.find('a', class_='external-source tm-event ga-event')['href']
        news_header = article.find('h2').text
        if 'día' not in published_date:
            title_link.append(f'<a href="www.meneame.net{link}">{news_header}</a><br>')
    return title_link
