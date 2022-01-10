import requests
from bs4 import BeatifulSoup
lapa = requests.get("http://vilanuvidusskola.blogspot.com/")
print(lapa)
print(lapa.content)


soup = BeatifulSoup(lapa.content, 'html.parser')
print(soup.prettify())