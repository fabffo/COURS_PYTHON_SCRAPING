#écrire un script qui extrait les infos d'une page
#Écrivez les données dans un fichier CSV qui utilise les champs comme en-têtes de colonnes
#Puis extraire et écrire csv pour une catégorie
#Puis extraire et écrire pour l'ensemble des catégories 1catégorie=1csv

import requests
from bs4 import BeautifulSoup
import time
"""links = []

#Boucle sur la totalité des pages
for i in range(1):
    i += 1
    urlOrigin = 'http://books.toscrape.com/catalogue/'
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    response = requests.get(url)
    #print(url)

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

            #on récupère la page article
            url_article = urlOrigin + link
            response_article = requests.get(url_article)
            #print(url_article)
            if response_article.ok:
                page = (BeautifulSoup(response_article.text, features="html.parser"))
                product_page_url = str(i)


                lignes = page.find_all('tr')
                #print(lignes)
                for ligne in lignes:
                    #print(ligne)
                    typeTexte = ligne.find('th')

                    # UPC
                    if typeTexte.string == 'UPC':
                        universal_product_code = ligne.find('td').text
                        print(universal_product_code)

                    # price_including_tax
                    if typeTexte.string == 'Price (incl. tax)':
                        price_including_tax = ligne.find('td').text.replace('Â', '')
                        print(price_including_tax)

                    # price_excluding_tax
                    if typeTexte.string == 'Price (excl. tax)':
                        price_excluding_tax = ligne.find('td').text.replace('Â', '')
                        print(price_excluding_tax)

                    # number_available
                    if typeTexte.string == 'Availability':
                        number_available = ligne.find('td').text
                        print(number_available)

                   # category
                    if typeTexte.string == 'Product Type':
                        category = ligne.find('td').text
                        print(category)

                   # review_rating
                    if typeTexte.string == 'Number of reviews':
                        review_rating = ligne.find('td').text
                        print(review_rating)

                # image_url
                image_url = page.find('img')
                image = image_url['src']
                print(image)


                #Titre
                titre = page.find('div', {'class':'col-sm-6 product_main'}).h1.text
                print(titre)

    with open('categorie.csv', 'w') as outf:
        outf.write('product_page_url' + ',' + 'UPC' + ',' +  'title' + ',' + 'price including tax' + ',' + 'price excluding tax' + ',' + 'number available' + ',' + 'category' + ',' + 'review_rating' + ',' + 'image\n')
        outf.write(product_page_url + ',' + universal_product_code + ',' + titre + ',' + price_including_tax + ',' + price_excluding_tax + ',' + number_available + ',' + category + ',' + review_rating + ',' + image)


        #On temporise 1 seconde pour ne pas se faire sortir
        time.sleep(1)

print(links)"""


#Puis extraire et écrire csv pour une catégorie
#<div class="side_categories">
#categories =[]

#Récupérer toutes les url catégories
url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
categorie_url = 'http://books.toscrape.com/catalogue/category'
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")
    categories = soup.find('ul', {'class': 'nav nav-list'})
    categorie = categories.find_all('li')
    for cat in categorie:
        a = cat.find('a')
        link = a['href'].replace('..', '')
        print(categorie_url+link)

