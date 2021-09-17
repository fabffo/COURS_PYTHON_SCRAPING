#écrire un script qui extrait les infos d'une page
#Écrivez les données dans un fichier CSV qui utilise les champs comme en-têtes de colonnes
#Puis extraire et écrire csv pour une catégorie
#Puis extraire et écrire pour l'ensemble des catégories 1catégorie=1csv
#book;url
import csv
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
                        #print(universal_product_code)

                    # price_including_tax
                    if typeTexte.string == 'Price (incl. tax)':
                        price_including_tax = ligne.find('td').text.replace('Â', '')
                        #print(price_including_tax)

                    # price_excluding_tax
                    if typeTexte.string == 'Price (excl. tax)':
                        price_excluding_tax = ligne.find('td').text.replace('Â', '')
                        #print(price_excluding_tax)

                    # number_available
                    if typeTexte.string == 'Availability':
                        number_available = ligne.find('td').text
                        #print(number_available)

                   # category
                    if typeTexte.string == 'Product Type':
                        category = ligne.find('td').text
                        #print(category)

                   # review_rating
                    if typeTexte.string == 'Number of reviews':
                        review_rating = ligne.find('td').text
                        #print(review_rating)

                # image_url
                image_url = page.find('img')
                image = image_url['src']
                #print(image)


                #Titre
                titre = page.find('div', {'class':'col-sm-6 product_main'}).h1.text
                #print(titre)

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
"""url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
categorie_url = 'http://books.toscrape.com/catalogue/category'
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")
    categories = soup.find('ul', {'class': 'nav nav-list'})
    categorie = categories.find_all('li')
    for cat in categorie:
        a = cat.find('a')
        link = a['href'].replace('..', '')
        print(categorie_url+link)"""

#On récupère une page et on l'analyse
#Extraire le titre de la page
#         le nombre de pages
#Pour chaque page les urls des livres de  la page
def urllivres(url):
    listL0 = []
    listL1 = []
    response = requests.get(url)
    #print(url)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        nbrpages = 0
        if soup.find('ul', {'class': 'pager'}):
            pages = soup.find('ul', {'class': 'pager'}).find('li', {'class': 'current'})
            pages = (str.rstrip(str.lstrip(pages.text))).replace('Page 1 of ', '')
            nbrpages = int(pages)
        #print(pages)


        #listes des pages du cataloue
        nompage = url.replace('index.html', '')
        list_pages = []

        #plusieurs pages donc index de page
        if nbrpages > 0:
            for i in range(nbrpages):
                j = i + 1
                urlpages = nompage + 'page-' + str(j) + '.html'
                list_pages.append(urlpages)
        else:
            #1 seule page donc pas d'index
            list_pages.append(url)

        for urlpage in list_pages:
            listL0 =  page(urlpage)
            listL1 = listL1 + listL0

        return listL1



#On extrait les informations des livres d'une page catalogue
def page(url):
    listLivres =[]
    links = []
    urlOrigin = 'http://books.toscrape.com/catalogue/'
    response = requests.get(url)
    # print(url)

    # On récupère une page et on l'analyse
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        articles = soup.find_all('article')

        for article in articles:
            #print(article)
            a = article.find('a')
            link = a['href']
            link = link.replace('../', '')
            #print(link)
            links.append(urlOrigin + link)

            # on récupère la page article
            url_article = urlOrigin + link
            response_article = requests.get(url_article)
            #print(url_article)
            if response_article.ok:
                page = (BeautifulSoup(response_article.text, features="html.parser"))
                product_page_url = url_article

                lignes = page.find_all('tr')
                # print(lignes)
                for ligne in lignes:
                    # print(ligne)
                    typeTexte = ligne.find('th')

                    # UPC
                    if typeTexte.string == 'UPC':
                        universal_product_code = ligne.find('td').text
                        #print(universal_product_code)

                    # price_including_tax
                    if typeTexte.string == 'Price (incl. tax)':
                        price_including_tax = ligne.find('td').text.replace('Â', '')
                        #print(price_including_tax)

                    # price_excluding_tax
                    if typeTexte.string == 'Price (excl. tax)':
                        price_excluding_tax = ligne.find('td').text.replace('Â', '')
                        #print(price_excluding_tax)

                    # number_available
                    if typeTexte.string == 'Availability':
                        number_available = ligne.find('td').text
                        #print(number_available)

                    # category
                    if typeTexte.string == 'Product Type':
                        category = ligne.find('td').text
                        #print(category)

                    # review_rating
                    if typeTexte.string == 'Number of reviews':
                        review_rating = ligne.find('td').text
                        #print(review_rating)

                # image_url
                image_url = page.find('img')
                image = image_url['src']
                #print(image)

                # Titre
                titre = page.find('div', {'class': 'col-sm-6 product_main'}).h1.text
                #print(titre)

                dicoLivre = {}
                dicoLivre['product_page_url'] = product_page_url
                dicoLivre['UPC'] = universal_product_code
                dicoLivre['title'] = titre
                dicoLivre['price including tax'] = price_including_tax
                dicoLivre['price excluding tax'] = price_excluding_tax
                dicoLivre['number available'] = number_available
                dicoLivre['category'] = category
                dicoLivre['review_rating'] = review_rating
                dicoLivre['image'] = image

            listLivres.append(dicoLivre)

    return listLivres

#Liste des catalogues
def dcatalogue():
    links = []
    listL0 = []
    listL1 = []

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
            res = soup.find('ul', {'class': 'nav nav-list'})
            res = res.find_all('li')
            for re in res:
                dicoCatalogue = {}
                ref = re.find('a')['href']
                #print(ref)
                catalogue = re.find('a').text
                dicoCatalogue['nom'] = str.rstrip(str.lstrip(catalogue))
                dicoCatalogue['href'] = urlOrigin+ ref
                listL0.append(dicoCatalogue)

    return listL0

#Lister tous les catalogues
catalogues = dcatalogue()
#print(catalogues)
listNom = []
listUrl = []
for catalogue in catalogues:
    listNom.append(catalogue['nom'])
    listUrl.append(catalogue['href'])
#print(listNom)
# Créer une liste pour les en-têtes
en_tete = ["nom", "url"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('catalogues.csv', 'w') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=',')
   writer.writerow(en_tete)
   # Parcourir les noms et urls - zip permet d'itérer sur deux listes ou plus à la fois
   for nom, url in zip(listNom, listUrl):
      # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
      ligne = [nom, url]
      writer.writerow(ligne)


#Extraire toutes les urls livres de l'ensemble des catégories
listeCatalogues = []
for catalogue in catalogues:
    if catalogue['nom'] != 'Books':
        print(catalogue['nom'] )
        if catalogue['nom'] in ('Travel', 'Mystery'):
            ensembleCatalogue = {}
            ensembleCatalogue['nom'] = catalogue['nom']
            ensembleCatalogue['livres'] = urllivres(catalogue['href'])
            listeCatalogues.append(ensembleCatalogue)
            # print(catalogue['href'])
#print(listeCatalogues)

# Créer une liste pour les en-têtes
en_tete = 'product_page_url' + ',' + 'UPC' + ',' +  'title' + ',' + 'price including tax' + ',' + 'price excluding tax' + ',' + 'number available' + ',' + 'category' + ',' + 'review_rating' + ',' + 'image'

for listeCatalogue in listeCatalogues:
    print("====================================")
    print(listeCatalogue['nom'])
    livres = (listeCatalogue['livres'])
    nom_catalogue = listeCatalogue['nom']+'.csv'
    # Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
    with open(nom_catalogue, 'w') as fichier_csv:
        # Créer un objet writer (écriture) avec ce fichier
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
    for livre in livres:
        listLignes = []
        for value in livre.values():
            listLignes.append(value)
        print(listLignes)
        with open(nom_catalogue, 'a') as fichier_csv:
            # Créer un objet writer (écriture) avec ce fichier
            writer = csv.writer(fichier_csv, delimiter=',')
            writer.writerow(listLignes)
""""
# Créer une liste pour les en-têtes
en_tete = ["nom", "url"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('catalogues.csv', 'w') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=',')
   writer.writerow(en_tete)
   # Parcourir les noms et urls - zip permet d'itérer sur deux listes ou plus à la fois
   for nom, url in zip(listNom, listUrl):
      # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
      ligne = [nom, url]
      writer.writerow(ligne)"""


#Extraire toutes les urls livres d'une catégorie
"""url= 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
res = urllivres(url)
print(res)"""


#url ='http://books.toscrape.com/catalogue/category/books/romance_8/page-1.html'
#res = page(url)
#print(res)
