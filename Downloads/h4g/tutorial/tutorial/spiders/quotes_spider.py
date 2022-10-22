
from bs4 import BeautifulSoup 
import requests


search = 'Jose Fernandez-Pacheco'
url = 'https://www.google.com/search'

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/98.0.4'

}
parameters = {'q': search}

content = requests.get(url, headers = headers, params = parameters).text
soup = BeautifulSoup (content,'html.parser')

search = soup.find(id = 'search')
links = search.find_all('a')

try:
    for link in links:
        print(link['href'])
except KeyError:
    pass