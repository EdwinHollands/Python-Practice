import requests
from bs4 import BeautifulSoup

url = 'https://novaramedia.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

print(f"{soup.title.string} Headlines:")

# Find all article titles and their corresponding links
articles = soup.find_all('h2')
for index, article in enumerate(articles):
    title = article.get_text()
    link = article.find('a')['href'] if article.find('a') else 'No link available'
    print(f"{index + 1}: {title}\nLink: {link}\n")