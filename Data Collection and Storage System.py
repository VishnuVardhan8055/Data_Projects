# -------------------------------------- Data Collection and Storage System -------------------------------------------

# How to Collect the data ?

# By through APIs , Web Scraping , etc...,

# How to store the data ?

# Store the data in a Data-Base system .


#                ==============================   Web-Scraping =========================================


import requests
import bs4
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_waterfalls_in_India_by_height'
page = requests.get(url)

#soup = bs4.BeautifulSoup(page.text,'html')

soup = bs4.BeautifulSoup(page.text, features="lxml")


Table_List = soup.find_all('th')

ColumnData = [title.text.strip() for title in Table_List]


df = pd.DataFrame(columns = ColumnData)


ListOfTable_Data = soup.find_all('tr')

Row_data = []
Row_data.append(ColumnData)
for row in ListOfTable_Data[6:]:
    row_data = row.find_all('td')
    Each_Row_Data = [data.text.strip() for data in row_data]
    if len(Each_Row_Data) < len(df.columns):
          row_data += [None] * (len(df.columns) - len(Each_Row_Data))
    else:
        Row_data.append(Each_Row_Data[1:-1])



Dataframe = pd.DataFrame(Row_data)



Dataframe.to_csv(r'/Users/vishnu/PycharmProjects/Data Engineering Projects/List Of Water Falls.csv')


