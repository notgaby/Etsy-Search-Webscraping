from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import json
import pprint
import re
from PIL import Image
import os


###NEW
#FOR LOOP HREF LINKS
#MAKE BROWSER SEARCH THOSE LINKS IN FOR LOOP (ITERATE THROUGH ARRAY OF LISTS -> TEXTFILE EXPORT)
#GET DATA
#CLOSE BROWSER


#wait for JS
browser = webdriver.Chrome(executable_path='C:/Users/othscs017/IdeaProjects/Etsy/lib/chromedriver.exe')
browser.get("https://www.etsy.com/search?q=back+to+school+sign+printable&explicit=1&ref=guided_search_1_1&guided_search=1")
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

#javascript
js_text = soup.findAll('script', charset="utf-8", type="text/javascript")
start = '3c65557fa67e42dc'
end = 'is_mweb_faves_in_search'
strng = str(js_text[1])
adClass = strng[strng.find(start)+len(start):strng.rfind(end)]
adClass = adClass[3:19]
str(adClass)
print('type: ',type(adClass))




#prices

"""
prices = []
for pr in soup.select(".n-listing-card__price"):
    strike = pr.find(class_='strike-through')
    if pr is strike:
        prices.append(pr.get_text())
print("prices: ",prices)
"""


#prices
fullPrices = []

for pr in soup.select(".n-listing-card__price"):
    death = pr.find(class_='strike-through')
    if death:
        strike = [s.get_text() for s in death.select(".currency-value")]
    else:
        etext = [e.get_text() for e in soup.select(".n-listing-card__price")]

fullPrices.extend(strike)
fullPrices.extend(etext)

print(len(fullPrices))


images = [i.get_text() for i in soup.select(".width-full.display-block.position-absolute")]
productTitle = [t.get_text() for t in soup.select(".text-gray.text-truncate.mb-xs-0.text-body")]

Imagelinks = []
for i in soup.select(".width-full.display-block.position-absolute"):
    Imagelinks.append(i['src'])

dirtyShopTitle = [title.get_text() for title in soup.select(".text-gray-lighter.text-body-smaller.display-inline-block")]
cleanShopTitle = []

for i in dirtyShopTitle:
    if "(" not in i:
        cleanShopTitle.append(i)

listingLink = []

print("Adclass", adClass)

#for price in (soup.findAll(False,{'class':['strike-through']}) and soup.findAll(True,{'class':['.n-listing-card__price']})) or (soup.findAll(True,{'class':['strike-through']}))

for tp in soup.findAll(True,{'class':['organic-impression',adClass]}):
    listingLink.append(tp['href'])


print('llll', len(listingLink))
"""
for tp in soup:
    if tp.find(class_='organic-impression') is not None or tp.find(class_=adClass) is not None:
        listingLink.append(tp['href'])

print('llll', listingLink)
"""
BTS = pd.DataFrame(
    {
        "shop": cleanShopTitle,
        "image": Imagelinks,
        "product title": productTitle,
        "listing link": listingLink

        #"prices ": fullPrices
    }
)

BTS.to_csv('example2.csv')

Links = pd.DataFrame(
    {
        "link": listingLink
    }
)
Links.to_csv('links.csv')

print(BTS)


images = pd.DataFrame(
    {
        "image":Imagelinks
    }
)

images.to_csv('images.csv')

prices = pd.DataFrame(
    {
        "prices": fullPrices
    }
)



##saves images



browser.close()
