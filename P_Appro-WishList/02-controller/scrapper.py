# import modules
import csv
import requests

# add lib
from bs4 import BeautifulSoup

with open("https://www.parfumdo.com/87-parfum-femme") as pageToParse:
    fetchedDatas = BeautifulSoup(pageToParse)
    fetchedDatas = BeautifulSoup("<span class=\"product-category\">MISS DIOR</span>", 
                                 "<span class=\"product-brand\"> Dior </span>", 
                                 "<span class=\"product-name\"> Eau de Parfum </span>",
                                 "<img src=<\"https://www.parfumdo.com/53987-home_default/miss-dior-eau-de-parfum.jpg\" alt=\"MISS DIOR Eau de Parfum\" loading=\"lazy\">",
                                 "<a href=\"https://www.parfumdo.com/417545-miss-dior-eau-de-parfum.html\" title=\"MISS DIOR Eau de Parfum\" class=\"\"> <span class=\"product_img_link\"> <img src=\"https://www.parfumdo.com/53987-home_default/miss-dior-eau-de-parfum.jpg\" alt=\"MISS DIOR Eau de Parfum<\" loading=\"lazy\"> </span> </a>")

# Parfumdo struct. 1page = 1prod
#
# Nom
#   <span class="product-category">MISS DIOR</span>
# Marque
#   <span class="product-brand"> Dior </span>
# Carac.
#   <span class="product-name"> Eau de Parfum </span>
# Prix
#   <span class="hidden"> 56.06 </span>
# IMG
#   <img src="https://www.parfumdo.com/53987-home_default/miss-dior-eau-de-parfum.jpg" alt="MISS DIOR Eau de Parfum" loading="lazy">
# Lien
#   <a href="https://www.parfumdo.com/417545-miss-dior-eau-de-parfum.html" title="MISS DIOR Eau de Parfum" class=""> 
#   <span class="product_img_link"> <img src="https://www.parfumdo.com/53987-home_default/miss-dior-eau-de-parfum.jpg" 
#   alt="MISS DIOR Eau de Parfum" loading="lazy"> </span> </a>