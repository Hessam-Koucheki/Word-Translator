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
    meaning = str(meaning)
    meaning = re.sub(r'\s+', ' ', meaning) # remove whitespaces
    meaning = re.sub(r'<.+?>', ' ', meaning) # remove tags and spans
    meaning = re.sub(r'\d+', ' ', meaning) # remove numbers from start
    meaning = re.sub('\.', ' ', meaning) # remove dot from start
    meaning = meaning.strip() # remove any extra left whitespaces
    print(meaning)

# print(soup)