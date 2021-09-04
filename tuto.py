import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

response = requests.get(url)

if response.ok:
    links = []
    soup = BeautifulSoup(response.text, features="html.parser")
    articles = soup.find_all('article')
    for article in articles:
        #print(article)
        a = article.find('a')
        link = a['href']
        #print(link)
        links.append(url + link)
    print(links)