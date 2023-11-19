import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.century21.com/real-estate-agents/new-jersey/LSNJ/'
DOMINIO = 'https://www.century21.com'
LINKS = []


def encontrando_links():
    resposta = requests.get(URL)
    link = BeautifulSoup(resposta.text, "html.parser")
    link1 = link.find('div', class_="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3")
    cards = link1.find_all('a')

    for card in cards:
        href = card['href']
        cleaned_href = re.sub(r'tel:\d+', '', href)
        print(cleaned_href)



















