import requests  # 1. O "Entregador" que busca o site
from bs4 import BeautifulSoup  # 2. A "Pinça" que limpa o HTML

# 3. O "Disfarce" completo para evitar bloqueios do R7 e CNN
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# 4. A "MÁQUINA" DE PEGAR NOTÍCIAS (Função)
# Ela recebe a URL e o Nome do site e faz todo o trabalho sujo
def pegar_noticias(nome_site, url_site, tag_alvo):
    try:
        # Busca o site
        resposta = requests.get(url_site, headers=headers, timeout=10)
        # Organiza o código do site
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        print(f"📌 Portal: {nome_site}")
        
        # Procura todos os textos daquela tag (ex: h2 ou h3)
        manchetes = soup.find_all(tag_alvo)
        
        contador = 0
        for item in manchetes:
            texto = item.get_text().strip()
            # Só mostra se o texto for grande (evita pegar menus ou botões)
            if len(texto) > 40 and contador < 3:
                contador += 1
                print(f"  {contador}. {texto}")
        
        print("-" * 40)
        
    except:
        print(f"❌ Erro ao acessar o site {nome_site}")

# 5. O COMANDO FINAL: Chamamos a máquina para cada site
print("🚀 BUSCANDO ÚLTIMAS NOTÍCIAS...\n")

# No G1 as notícias principais costumam ser links (a)
pegar_noticias("G1 Globo", "https://globo.com", "a")

# No R7 as notícias principais são títulos (h3)
pegar_noticias("R7 Record", "https://r7.com", "h3")

# Na CNN as notícias principais são títulos (h2)
pegar_noticias("CNN Brasil", "https://cnnbrasil.com.br", "h2")

print("✅ Busca finalizada!")
