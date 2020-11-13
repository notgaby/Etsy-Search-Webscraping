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
import csv
from PIL import Image
import os
import urllib.request


##### opens link file and puts it in an array
links = []
imageLinks = []
with open('links.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        links.append(row[1])
links.pop(0) #delete the 'links' title
#print(links)

imageLinks = []
with open('images.csv') as pics:
    readImages = csv.reader(pics, delimiter=',')
    for row in readImages:
        imageLinks.append(row[1])
imageLinks.pop(0)
print(len(imageLinks))

for i in range(0, (len(imageLinks)-1)):
    os.chdir(r"C:\Users\othscs017\IdeaProjects\EtsySearchFin\pictures")
    name = str(i)+".jpg"
    urllib.request.urlretrieve(imageLinks[i],name)



##### for loop opens webpages
browser = webdriver.Chrome(executable_path='C:/Users/othscs017/IdeaProjects/Etsy/lib/chromedriver.exe')
for i in range(0,(len(links)-1)):

    browser.get(links[i])
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')

browser.close()

