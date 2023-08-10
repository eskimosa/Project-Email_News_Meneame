from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
import smtplib
import schedule
import time

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


def email():
    email_address = os.environ.get('gmail_address')
    email_password = os.environ.get('gmail_password')

    results = scrape_news()

    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = 'esskimosa@gmail.com'
    message['Subject'] = 'Your daily news!'

    for i in results:
        message.attach(MIMEText(i, 'html'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(message)

'''
schedule.every(10).seconds.do(email)

while True:
    schedule.run_pending()  # applies the schedule
    time.sleep(1)


Albert version
for article in news:
    link_div = article.find('div', 'content thumb')
    if link_div:
        link = link_div.find('a')
        print(link['href'])
    else:
        print('Article without link. Debug more...')
    published_date = article.find('span').text.replace('por', '')
    if 'día' not in published_date:
        print(published_date)
        news_header = article.find('h2').text
        print(news_header)
        print('-----------------------------------------------------------------------------')





for div in soup.find_all('div', 'content thumb'):
    for a in div.find_all("a"):
        print(a["href"])
        
        
if __name__ == '__main__':
    while True:
        find_news()

'''
