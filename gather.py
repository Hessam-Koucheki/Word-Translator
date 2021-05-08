import requests
from bs4 import BeautifulSoup as bs

# Load the whole webpage
page = requests.get('https://dic.b-amooz.com/en/dictionary/w?word=best')
soup = bs(page.text, 'html.parser')

# Grab appropriate section using quick access menu
val = soup.find_all('a', attrs={'class' : 'quick-access-items'} )
print(val)
# print(soup)