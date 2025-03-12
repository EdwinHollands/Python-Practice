import requests
from bs4 import BeautifulSoup
url = 'https://novaramedia.com/'
r=requests.get(url)
r_html=r.text
soup = BeautifulSoup(r_html, 'html.parser')
print(f"{soup.title.string} Headlines:")
titles = soup.find_all('h2')
for title in titles:
    print(f"{titles.index(title)+1}: {title.get_text()}")