vagas_selecionadas=[]

for i in range(3):
    titulo_vaga=input('Qual o titulo da Vaga: ')
    linguagem=input(f'Qual a linguagem principal para a vaga de {titulo_vaga}: ')

    if (linguagem == 'python') or (linguagem == 'Python'):
        vagas_selecionadas.append(titulo_vaga)
        print('Essa vaga é perfeita para o meu portfólio!')
    else:   
        print('Essa não é de Python, vamos pular.')    

print(f'Vagas para eu me candidatar: {vagas_selecionadas}')
