# import modules
import csv
import requests

# add lib
from bs4 import BeautifulSoup

def scrap()
    {
        return fetchedDatas
    }

# Galaxus struct. 1page = 1prod
#
# Nom
#   <span class="sc-1l1ysqm-0 bDSRlN">AirPods Pro (2nd Gen.) MagSafe USB-C</span>
# Marque
#   <strong>Apple</strong>
# Carac.
#   <span class="sc-12r9jwk-1 fjTjcd">ANC, 6&nbsp;h, Sans fil</span>
# Prix
#   <span aria-label="225 CHF">225.–</span>
# IMG
#   <img class="sc-1ienw2c-1 jXozAl" src="/im/productimages/3/5/0/3/1/7/6/3/7/2/2/4/8/1/7/4/0/1/5/
#   b2efad0f-fc3a-4650-9d9b-3924bdf99e2b.jpg?impolicy=ProductTileImage&amp;resizeWidth=358&amp;resize
#   Height=358&amp;cropWidth=358&amp;cropHeight=358&amp;resizeType=downsize&amp;quality=high" decoding=
#  "auto" alt="Image du produit" loading="eager">