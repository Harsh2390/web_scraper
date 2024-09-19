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
data3 = scrape_detail_page(url3)
data4 = scrape_detail_page(url4)


while input != False:
    print("Your Options are:\n1. Top Losers\n2. Top Gainers\n3. 52 Week Gainers\n4. 52 Week Losers\n5. exit")
    user_input = input("Enter the name of the file you want to save the data to: ")

    if user_input == '':
        print("No file name entered")
    elif user_input == 'Top Losers':
        print("Top Losers")
        print(data)
        print("====================================================================================================================================================================================")
    elif user_input == 'Top Gainers':
        print("Top Gainers")    
        print(data2)
        print("====================================================================================================================================================================================")
    elif user_input == '52 Week Gainers':
        print("52 Week Gainers")
        print(data3)
        print("====================================================================================================================================================================================")
    elif user_input == '52 Week Losers':
        print("52 Week Losers")
        print(data4)
        print("====================================================================================================================================================================================")
    elif user_input == 'exit':
        input = False
    else:
        print("Invalid file name")





