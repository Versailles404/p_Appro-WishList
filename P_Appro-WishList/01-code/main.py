import csv
import requests
import os
from bs4 import BeautifulSoup


#fonction GET
#param 1 = url de la page
#param 2 = page à scraper
def getPerfume(url, page):

    #variable qui lance une requête au site web avec la page en paramètre
    req = requests.get(url + '?p=' + str(page))

    #initialisation de la variable soup qui contient la page html
    soup = BeautifulSoup(req.text, "html.parser")

    # recadrage dans le scope du scraper pour vérifier s'il y ades éléments à parser
    perfumeList = soup.find('div', class_='content-product-list')

    # parassage des éléments
    perfumes = perfumeList.find_all('div', class_='product-container')

    # création s'il n'existe pas ou ouverture d'un fichier .csv
    with open('scrappyCSV.csv', 'a', newline='') as file:

        # initalisation de l'écriture du fichier avec comme délimiteur de colonne, le ;
        writer = csv.writer(file, delimiter=';')

        # boucle qui va chercher chaque élément correspondant aux métadonnées
        for perfume in perfumes:
            name = perfume.find('a', class_='product-link')['title']
            price = perfume.find('span', class_='segmented-price').text
            brand = perfume.find('span', class_='product-brand').text
            image = perfume.find('img')['src']
            lien = perfume.find('a', class_='product-link')['href']

            # écriture de la ligne d'information trouvée pour le parfum
            writer.writerow([name, price, brand, image, lien])

    # fonction récursive pour continuer tan qu'il y a des produits
    if(len(perfumes) == 0):
        # si plus de parfum, ne rien faire
        return
    else:
        # appel de la fonction pour passer à la page suivante
        getPerfume(url, page + 1)

# si le fichier n'existe pas, création du fichier et rajout des headers
if not os.path.exists('scrappyCSV.csv'):

    #création du fichier
    with open('scrappyCSV.csv', 'w', newline='') as file:

        # initalisation de l'écriture du fichier avec comme délimiteur de colonne, le ;
        writer = csv.writer(file, delimiter=';')

        # définition des métadonnées
        writer.writerow(['Nom', 'Prix', 'Marque', 'Image', 'Lien'])


#appel de la fonction GET, getPerfume
getPerfume('https://www.parfumdo.com/en/79-perfume', 1)
