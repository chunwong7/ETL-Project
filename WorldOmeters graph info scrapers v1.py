import requests
import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup

#https://www.worldometers.info/coronavirus/

#https://www.worldometers.info/coronavirus/country/us/

""" Worldometers.info	Web scrape	
Total cases, new cases(per day), total deaths, 
new deaths, active cases, total cases/1M pop, deaths/1M pop, 
total tests, tests/1M pop
 """

#the request (needs to be 200)
result = requests.get("https://www.worldometers.info/coronavirus/country/us/")

src = result.content
soup = BeautifulSoup(src, 'html.parser')

table = soup.find_all('table')

state_list = []

#html by id tag
table_data = soup.find(id="usa_table_countries_today")

#html by style tags
table_data = table_data.find_all(style = ["font-weight: bold; text-align:right","text-align:right;font-weight:bold;",\
"font-weight: bold; text-align:right;","font-weight: bold; text-align:right;background-color:#FFEEAA;","font-weight: bold; text-align:right;background-color:red; color:white"] )
#six_day = table_data.find_all('td')
print(table_data)


#for loop to strip the tags from the HTML
for data in table_data:
    

    data = data.text
    data = data.replace(',', '')
    data = data.replace(' ', '')
    data = data.strip('\n')
    #data = int(data,4) 
    
    #data = int(data,8)
    
    print(data)
    state_list.append(data) #stripping the '\n' from the data


#Used another scraper in different file to pull all states and append to a list

#list of the states for the dataframe rows
list_of_states = ['New York ', 'New Jersey ', 'Massachusetts ', 'California ', 'Pennsylvania ', 'Illinois ', 'Michigan ', 'Florida ', 'Louisiana ', 'Connecticut ', 'Texas ', 'Georgia ', 'Maryland ', 'Ohio\
', 'Indiana ', 'Washington ', 'Colorado ', 'Virginia ', 'Tennessee ', 'North Carolina ', 'Missouri ', 'Rhode Island ', 'Alabama ', 'Arizona ', 'Mississippi ', 'Wisconsin ', 'South Carolina ', 'Nevada ', 'Iowa\
', 'Utah ', 'Kentucky ', 'District Of Columbia ', 'Delaware ', 'Oklahoma ', 'Minnesota ', 'Arkansas ', 'Kansas ', 'New Mexico ', 'Oregon ', 'Nebraska ', 'South Dakota\
', 'Idaho ', 'New Hampshire ', 'West Virginia ', 'Maine ', 'Vermont ', 'North Dakota ', 'Hawaii ', ' Wyoming ', 'Montana ', 'Alaska ']

#column list for the dateframe columns
list_of_columns = ["Total Cases", "New Cases", "Total Deaths", "New Deaths", "Active Cases", "Total Cases per million", "Deaths per million", "Total tests", "Tests per million"]

state_list = state_list[:459] #intentially cutting string values off to eliminate US territories and crusie ships in the data

df = pd.DataFrame(np.array(state_list).reshape(51,9), index= list_of_states, columns = list_of_columns) #turns the giant list of data into a 51x9 dataframe with the columns and rows listed

df.index.name = "US States" #sets index name

print(df)

news_date = soup.find(style="font-size:13px; color:#999; text-align:center") #find the date and time in GMT time
news_date = news_date.text #strip the HTML tags
news_date = news_date.strip("Last updated: ") # removes the Last Updated part of text


#stripping the time string of spaces and colon
news_date = news_date.replace(' ', '')
news_date = news_date.replace(':', '')

csv_string = "D:\\Users\\Goutham\\Documents\\ETL Project\\" + str(news_date) + ".csv"

#creating and uploading dataframe to csv file with the name of the date and time
df.to_csv(csv_string)
#df.columns = df.columns.str.strip()
#cols = ['col1', 'col2', 'col3']
#data['Total Cases'] = data['Total Cases'].apply(pd.to_numeric, errors='ignore', axis=1, downcast = "integer")

print(csv_string)
print(df.dtypes)