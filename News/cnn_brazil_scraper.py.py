import requests
from bs4 import BeautifulSoup

url = 'https://www.cnnbrasil.com.br/'
# Adicionamos um "disfarce" para o site achar que somos um navegador comum
headers = {'User-Agent': 'Mozilla/5.0'} 

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Vamos tentar pegar TODOS os títulos h2 do site, sem filtrar pela classe ainda
    manchetes = soup.find_all('h2')
    
   # Criamos uma lista com todas as etiquetas de título (h1 e h2)
    manchetes = soup.find_all(['h1', 'h2'])
    
    if not manchetes:
        print("A pinça não encontrou nenhum título.")
    else:
        print(f"Salvando {len(manchetes)} notícias no arquivo...")
        # 'w' significa write (escrever). O encoding garante que os acentos funcionem.
        with open("noticias_cnn.txt", "w", encoding="utf-8") as arquivo:
            for i, noticia in enumerate(manchetes[:30], 1):
                texto = noticia.text.strip()
                if texto:
                    arquivo.write(f"{i}. {texto}\n")
        print("Concluído! Verifique o arquivo noticias_cnn.txt na barra lateral.")
else:
    print(f"Erro de conexão: {resposta.status_code}")