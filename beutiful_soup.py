from bs4 import BeautifulSoup
import requests
import pandas as pd


html_data = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks').text

soup = BeautifulSoup(html_data, 'html.parser')

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    try:
        Name = col[1].find_all('a')[1].contents[0]
        Market_Cap = float(col[2].contents[0][:-1])
        data = data.append({"Name": Name,
                           "Market Cap (US$ Billion)": Market_Cap},
                           ignore_index=True)
    except:
        continue

data.to_json('bank_market_cap.json')
