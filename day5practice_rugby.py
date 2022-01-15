import requests
from bs4 import BeautifulSoup

url = 'https://www.skysports.com/rugbyleague/competitions/championship-one/tables'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.title.text)

table = soup.find('table', class_ = 'v5-tbl-t6 v5-tbl-t7 enable-lg-tbl')
#print (table)

headers = []
for i in table.find_all('th'):
    title = i.text 
    headers.append(title)

import pandas as pd

data = pd.DataFrame( columns= headers)

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(data)
    data.loc[length] = row

data.to_csv('rugby_table.csv',index=False)
df = pd.read_csv('rugby_table.csv')

#print(df)

#print(df.shape)
#print(df.describe())
#print(df.tail(3))
Pts = df['Pts']
Team = df.Team
df.replace('  ','').replace('\n','')

import matplotlib as mpl
import matplotlib.pyplot as plt
df.plot(kind='pie', figsize=(10, 6))

#plt.xlabel('Team') # add to x-label to the plot
#plt.ylabel('Pts') # add y-label to the plot
#plt.title('Rugby table') # add title to the plot

#plt.show()

df_pie = data.sort_values(by = 'Pts', ascending = False).head(5)
fig = px.pie(df_pie, values='Pts', names='Team', title='points vs Teams')
fig.show()
