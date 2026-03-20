oportunidades_reais=[]


for n in range(3):
  nome_loja=input('\n Digite o nome da loja: ')
  preco_loja=float(input(f'\n Digite o valor do Iphone que você procura na loja {nome_loja}: '))

  if preco_loja < 5000:

    oportunidades_reais.append(f'O preço do Iphone na loja {nome_loja} é {preco_loja} está dentro do orçamento!')
      
  else:
    print(f'\n Muito caro na {nome_loja} ta fora do orçamento!')

print(f'\n Essa foram as oportunidades encontradas: {oportunidades_reais}')

        
        