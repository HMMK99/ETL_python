from bs4 import BeautifulSoup
import requests
import os
import re
from googletrans import Translator

agent = {"User-Agent":"Mozilla/5.0"}
html_data = requests.get('https://www.classcentral.com', headers=agent).text
soup = BeautifulSoup(html_data, 'html.parser')

all_links = soup.find_all('a')

for url in all_links:
  if '.com' in url['href']:
    site = requests.get(url['href'], headers=agent).text
  else:
    site = requests.get('https://www.classcentral.com'+url['href'],
                        headers=agent).text

# Still in progress
translator = Translator(service_urls=['translate.googleapis.com'])

result = translator.translate('content to translate', src='en', dest='hi')
