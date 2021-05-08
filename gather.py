from os import makedev
import requests
from bs4 import BeautifulSoup
import re

# Load the whole webpage
page = requests.get('https://dic.b-amooz.com/en/dictionary/w?word=best')
soup = BeautifulSoup(page.text, 'html.parser')

# Grab appropriate section using quick access menu
meanings = soup.find_all('a', attrs={'class' : 'quick-access-items'} )
# print(val[2])

for meaning in meanings:
    # print(str(meaning)) 
    print(re.sub(r'\s+', ' ', str(meaning)))
    print('------------------')

# print(soup)