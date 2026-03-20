# Dados brutos que o sistema te entregou:
estoque_bruto = [
    ["Televisão 4K", 2500],
    ["Cabo HDMI", 40],
    ["Notebook Gamer", 5500],
    ["Mouse Pad", 30],
    ["Teclado Mecânico", 200],
    ["Adaptador USB", 15]
]


lista_promocao=[]


for produto in estoque_bruto:
    nome_prod=produto[0]
    preco_prod=produto[1]

    if preco_prod < 100:
        print(f'\n O produto {nome_prod} custa {preco_prod} está barato!')
        lista_promocao.append(produto)

qtd_baratinho=len(lista_promocao)

print(f'\n O Marketing pode anunciar {qtd_baratinho} produtos baratinhos!')
print(f'\n Produtos para promoção: {lista_promocao}\n')
