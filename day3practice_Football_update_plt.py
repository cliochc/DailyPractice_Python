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
#print(mydata2.shape)
#print(mydata2.describe())
#print(mydata2.Team)

#mydata.reset_index('Team', inplace=True)
#print(mydata[mydata.index =='\nChelsea\n'])
#print(mydata.loc['\nWest Ham United\n'])
#df_list = mydata.sort_values(by = 'Pts', ascending = True)
#print(df_list.head(5))


import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#fig = go.Figure(data=go.Scatter(x=df_list['Team'], y=df_list['Pts'], mode='markers', marker=dict(color='red')))
# Updating layout through `update_layout`. Here we are adding title to the plot and providing title to x and y axis.
#fig.update_layout(title='points vs teams', xaxis_title='name', yaxis_title='points')
# Display the figure
#fig.show()

df_pie = mydata.sort_values(by = 'Pts', ascending = False).head(5)

fig = px.pie(df_pie, values='Pts', names='Team', title='points vs Teams')
fig.show()