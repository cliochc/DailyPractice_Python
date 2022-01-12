import requests
from bs4 import BeautifulSoup
import os

url ='https://www.airbnb.ca/rooms/49983159?category_tag=Tag%3A8173&adults=1&children=0&infants=0&check_in=2022-08-01&check_out=2022-08-08&federated_search_id=06cfe0e3-563b-4c70-8628-21e422f9c0e9&source_impression_id=p3_1642026348_giZdCMYRZ6aY4lcu'

r = requests.get(url)

#print(r.status_code)

soup =  BeautifulSoup(r.text, 'html.parser')
#print(soup.title.text)
#print(soup.prettify())

#p = soup.find('span',{'class' : '_1gw6tte'})
#print(p)

images = soup.find_all('img')
#print(images)
for image in images:
    print(image['alt'])  
    name = image['alt']
    link = image['src']
    with open(name.replace(' ','-').replace('/','') + '.jpg','wb') as f:
        im = requests.get(link)
        f.write(im.content)
        #print('Writing', name)
