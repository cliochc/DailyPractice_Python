import requests
from bs4 import BeautifulSoup

url = 'https://www.skysports.com/premier-league-table'

r = requests.get(url)
#print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.title.text)
#print(soup)

league_table = soup.find('table', class_ = 'standing-table__table')
#print (league_table)

import pandas as pd

headers= []
for i in league_table.find_all('th'):
    title = i.text
    headers.append(title)

mydata = pd.DataFrame(columns = headers)


for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td',class_ = 'standing-table__cell standing-table__cell--name').text.strip()
        pl_prints = row.find_all('td',class_ = 'standing-table__cell')[2].text
        #print(pl_team,pl_points)


import pandas as pd

headers= []
for i in league_table.find_all('th'):
   title = i.text
   headers.append(title)

mydata = pd.DataFrame(columns = headers)


for j in league_table.find_all('tr')[1:]:
   row_data = j.find_all('td')
   row = [i.text for i in row_data]
   length = len(mydata)
   mydata.loc[length]= row

mydata.to_csv('league_table.csv', index=False)
# Try to read csv
mydata2 = pd.read_csv('league_table.csv')

#print(mydata2)

import numpy as np 
#print(mydata2.head())
mydata2.shape


