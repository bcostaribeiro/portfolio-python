videos_para_assistir = []

for i in range(3):
    titulo_video = input('Qual o titulo do video que o robô encontrou: ')
    visualizacoes=int(input(f'Quantas visualizações tem o video {titulo_video} ? '))

    if (titulo_video =='ia') and (visualizacoes > 10000):
        videos_para_assistir.append(titulo_video)  
        print('\n Video relevante Encontrado! \n')  
    else:
        print('\n Não é relevante! xá pra lá! \n')    


print(f'Lista de videos pra assistir {videos_para_assistir}')