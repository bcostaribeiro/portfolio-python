import requests # 1. O "Entregador" que vai buscar os dados na API


# --- CONFIGURAÇÃO ---
API_KEY = 'YOUR_KEY_HERE'  # <-- COLE SUA CHAVE ENTRE AS ASPAS
PAIS = 'us'  # Código para buscar notícias do Brasil

def buscar_top_virais():
    """Função que conecta na API e traz as notícias mais quentes do momento."""
    
    # 2. Endereço da API filtrando por "Principais Manchetes" do Brasil
    url = f'https://newsapi.org/v2/top-headlines?country={PAIS}&apiKey={API_KEY}'

    

   
    try:
        # 3. O Python faz o pedido e recebe um arquivo "JSON" (tipo uma lista organizada)
        resposta = requests.get(url)
        dados = resposta.json()
        
        # 4. Verifica se o Google/NewsAPI autorizou o acesso
        if dados['status'] == 'ok':
            artigos = dados['articles']
            
            print(f"✅ Sucesso! Encontrei {len(artigos)} notícias bombando agora.\n")
            
            # 5. Mostramos as 5 primeiras (as mais importantes da capa)
                        # 5. Pegamos as 5 notícias MAIS QUENTES e extraímos tudo delas
            for i, noticia in enumerate(artigos[:5], 1):
                titulo = noticia['title']
                fonte = noticia['source']['name']
                link = noticia['url'] # Pega o endereço da matéria
                imagem = noticia.get('urlToImage') # Pega o link da foto
                
                # Exibição profissional e organizada no terminal
                print(f"🔥 VIRAL {i}: [{fonte}]")
                print(f"📌 TÍTULO: {titulo}")
                print(f"🔗 LINK: {link}")
                
                if imagem:
                    print(f"🖼️ IMAGEM: {imagem}")
                else:
                    print("🖼️ IMAGEM: (Sem imagem disponível)")
                
                print("-" * 50) # Linha separadora maior

        else:
            print("⚠️ Erro na API: Verifique se colou a chave corretamente.")
            
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    buscar_top_virais()
