import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/'
resposta = requests.get(url)

if resposta.status_code == 200:
    # A "pinça" entra em ação aqui
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Procuramos por todas as manchetes (que no G1 ficam em tags <a>)
    manchetes = soup.find_all('a', class_='feed-post-link')
    
    print("=== ÚLTIMAS NOTÍCIAS DO G1 ===")
    for i, noticia in enumerate(manchetes[:5], 1):
        print(f"{i}. {noticia.text}")
else:
    print("Não consegui acessar o site.")