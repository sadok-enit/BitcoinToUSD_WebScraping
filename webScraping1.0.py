# Import libraries
from lib2to3.pgen2.pgen import DFAState
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an URL object

# Create object page

headers = ['Date','Market Cap','Volume','Open','Close']
# Create a dataframe
mydata = pd.DataFrame(columns = headers)

for page_num in range(1,7):
    url = 'https://www.coingecko.com/en/coins/bitcoin/historical_data?page='+str(page_num)+'&start_date=2022-01-01'
    page = requests.get(url)



    soup = BeautifulSoup(page.text, 'lxml')

    # Obtain information from tag <table>
    table1 = soup.find('table', {'class':'table table-striped text-sm text-lg-normal'})

    # Obtain every title of columns with tag <th>
    
    #c=0
    #for i in table1.find_all('th'):
    #    title = i.text
    #    headers.append(title)
    #    c=c+1
    #    if (c==5):
    #        break

    
    # Create a for loop to fill mydata
    aux=table1.find('tbody')
    for j in aux.find_all('tr'):
        row_data = j.find_all()
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row

#print(mydata)
# Export to csv
mydata.to_csv('BitcoinToUSD.csv', index=False)
# Try to read csv
mydata2 = pd.read_csv('BitcoinToUSD.csv')













































# Obtain every title of columns with tag <th>

#headers = []
#for i in table1.find_all('th'):
#    title = i.text
#    headers.append(title)