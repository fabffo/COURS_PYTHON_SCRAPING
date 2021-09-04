import requests
from bs4 import BeautifulSoup
import time

links = []

#Boucle sur la totalité des pages
for i in range(50):
    urlOrigin = 'http://books.toscrape.com/'
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    response = requests.get(url)

   #On récupère une page et on l'analyse
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        articles = soup.find_all('article')

        for article in articles:
            # print(article)
            a = article.find('a')
            link = a['href']
            # print(link)
            links.append(urlOrigin + link)

        #On temporise 1 seconde pour ne pas se faire sortir
        time.sleep(1)

print(links)
