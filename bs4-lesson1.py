from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[0]
titles = table.find_all('th')
textTitles = [title.text.strip() for title in titles]

df = pd.DataFrame(columns = textTitles)


colms = table.find_all('tr')
for row in colms[1:]:
    row_data = row.find_all('td')
    indv_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = indv_row_data
df.to_csv('companies.csv', index = False)