import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_detail_page(url):
    try :
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Failed to fetch page: {response.status_code}')
            return None
        
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table', class_ = 'markets-table freeze-col yf-42jv6g fixedLayout')
        headers = table.find_all('th')
        titles = []
        for i in headers:
            title = i.text
            titles.append(title)


        df = pd.DataFrame(columns = titles)
        rows = table.find_all('tr')
        for i in rows[1:]:
            data = i.find_all('td')
            row = [tr.text for tr in data]
            length = len(df)
            df.loc[length] = row

        df = df.iloc[:, :-2]
        return df
        
    
        
    except Exception as e:
        print(f'Failed to fetch page: {e}')
        return None
         

url1 = 'https://finance.yahoo.com/markets/stocks/losers/'
url2 = 'https://finance.yahoo.com/markets/stocks/gainers/'
url3 = 'https://finance.yahoo.com/markets/stocks/52-week-gainers/'
url4 = 'https://finance.yahoo.com/markets/stocks/52-week-losers/'
data = scrape_detail_page(url1)
data2 = scrape_detail_page(url2)
print("Top Losers")
print(data)
print("====================================================================================================================================================================================")
print("Top Gainers")
print(data2)
print("====================================================================================================================================================================================")
print("52 Week Gainers")
data3 = scrape_detail_page(url3)
print(data3)
print("====================================================================================================================================================================================")
print("52 Week Losers")
data4 = scrape_detail_page(url4)
print(data4)





