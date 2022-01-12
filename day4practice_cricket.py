from pandas.core.algorithms import checked_add_with_arr
import requests
from bs4 import BeautifulSoup

url = 'https://www.skysports.com/cricket/tables'

r = requests.get(url)
#print(r.status_code)

soup = BeautifulSoup (r.text, 'html.parser')
#print(soup.title.text)
#print(soup)

c_table = soup.find('table', title = "ICC Men's T20 World Cup 2021 Group 1  ")
#print(c_table)

import pandas as pd

headers = []
for i in c_table.find_all('th'):
    title = i.text
    headers.append(title)

c_data = pd.DataFrame (columns = headers)




for j in c_table.find_all('tr')[1:]:
   row_data = j.find_all('td')
   row = [i.text for i in row_data]
   length = len(c_data)
   c_data.loc[length]= row
   
c_data.to_csv('cricketT20_table.csv', index=False)
c_data2 = pd.read_csv('cricketT20_table.csv')

#print(c_data2)
#print(c_data2.describe())
#print(c_data2.shape)

#print(c_data2.loc['\nEngland \n'])
#print(c_data2['TEAM'])
#print(c_data2[c_data2.index =='Australia'])
df_list = c_data2.sort_values (by = 'PTS', ascending= False)
print (df_list.head())

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=df_list['TEAM'], y=df_list['PTS'], mode='markers', marker=dict(color='red')))

fig.update_layout(title='ICC MEN T20 WORLD CRICKET', xaxis_title='TEAM', yaxis_title='points')

fig.show()
