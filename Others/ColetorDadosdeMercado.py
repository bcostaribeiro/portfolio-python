
produtos_baratos = []

for i in range(3):
    nome_prod=input('\n Digite o nome do Produto: ')
    preco_site_a=float(input(f'\n Digite o preço do {nome_prod} no site A: '))
    preco_site_b=float(input(f'\n Digite o preço do {nome_prod} no site B: '))

    if preco_site_a < preco_site_b:
        produtos_baratos.append(f'{nome_prod} no site A é mais barato!')
        print('\n Compre no Site A, é mais barato!')
        
    elif preco_site_a > preco_site_b:
        produtos_baratos.append(f'{nome_prod} no site B é mais barato!')
        print('\n Compre no Site B, é mais barato!')
     
    else: 
        produtos_baratos.append(f'{nome_prod} Tanto Faz os preços são iguais!')
        print('\n Os preços são iguais!')

print(f'\n Os produtos que valem a pena comprar são: {produtos_baratos} \n')

