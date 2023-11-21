import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

DOMINIO = 'https://www.century21.com'


def requisicao(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as error:
        print(error)


def parsing(soup):
    try:
        parse = BeautifulSoup(soup, 'html.parser')
        return parse
    except Exception as error:
        print(error)


def extrair_links(url):
    resposta = requisicao(url)
    soup = parsing(resposta)
    localizar = soup.find('div', class_='row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3')
    article = localizar.find_all('a')
    links = []
    for link in article:
        href = link.get('href')
        link_completo = urljoin(DOMINIO, href)
        link_alterado = re.sub("tel:\d+", " ", link_completo)
        links.append(link_alterado)
    # Remover strings vazias da lista
    return [link.strip() for link in links if link.strip()]


def obter_informacoes_agente(url):
    response = requests.get(url)
    soupa = parsing(response.text)


    h1 = soupa.find('h1', class_='h2')
    nome = h1.find('strong').text if h1 else ''


    div_telefone = soupa.find('div', class_='w-50 w-sm-100')
    telefone = div_telefone.find('a')['href'] if div_telefone else ''


    address_tag = soupa.find('address', {'data-turbo': 'true'})
    endereco = address_tag.get_text(strip=True, separator='\n') if address_tag else ''


    style_tag = soupa.find('span', class_="lead d-block")
    empresa = style_tag.text if style_tag else ''

    return {
        'nome': nome,
        'telefone': telefone,
        'endereco': endereco,
        'empresa': empresa
    }


def main():
    url_base = "https://www.century21.com/real-estate-agents/wildwood-nj/LCNJWILDWOOD/"
    links = extrair_links(url_base)

    for link in links:
        informacoes = obter_informacoes_agente(link)
        print(informacoes)
        print()


if __name__ == "__main__":
    main()