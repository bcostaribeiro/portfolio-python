# 1. Imagine que essa lista é o que o seu robô trouxe do site
noticias_da_internet = ["Neymar joga hoje", "Preço do dólar sobe", "Nova atualização do Python"]

# 2. O seu objetivo é guardar isso numa "Pasta de Trabalho"
pasta_de_trabalho = []

# 3. Vamos percorrer o que veio da internet e colocar na nossa pasta
for noticia in noticias_da_internet:
    print(f"Processando: {noticia}")
    pasta_de_trabalho.append(noticia)

# 4. AGORA A MÁGICA DA MANIPULAÇÃO (O que pedem em vagas):
# Se quisermos saber apenas a PRIMEIRA notícia que processamos:
print(f"A primeira notícia da minha pasta é: {pasta_de_trabalho[0]}")

# E se quisermos saber quantas notícias processamos no total?
total = len(pasta_de_trabalho)
print(f"No total, processei {total} notícias.")