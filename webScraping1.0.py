# Import libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = ['Date','Market Cap','Volume','Open','Close']
# Create a dataframe
mydata = pd.DataFrame(columns = headers)

for page_num in range(1,7):
    # Create an URL object
    url = 'https://www.coingecko.com/en/coins/bitcoin/historical_data?page='+str(page_num)+'&start_date=2022-01-01'
    # Create object page
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')

    # Obtain information from tag <table>
    table1 = soup.find('table', {'class':'table table-striped text-sm text-lg-normal'})
    
    # Create a for loop to fill mydata
    aux=table1.find('tbody')
    for j in aux.find_all('tr'):
        row_data = j.find_all()
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row

# Export to csv
mydata.to_csv('BitcoinToUSD.csv', index=False)
# Try to read csv
mydata2 = pd.read_csv('BitcoinToUSD.csv')


