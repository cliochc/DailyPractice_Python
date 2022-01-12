import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.skysports.com/cricket/news/12340/12514520/england-captain-joe-root-offers-renewed-support-to-chris-silverwood-ahead-of-final-ashes-test'
r = requests.get(url)
#print (r.status_code)

soup = BeautifulSoup (r.text, 'html.parser')
#print(soup)

#title_h1 = soup.find('h1', class_ ='article__title')
#print (title_h1.text)

images = soup.find_all('img')
#print(images)

p = soup.find_all('p')
#print(p)

