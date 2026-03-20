comentarios_aprovados=[]

for i in range(3):
    
    nome_usuario=input('\n Digite o seu Nome: ')
    texto_comentario=input('\n Comnetarios: ')

    if texto_comentario == 'palavrao':
        print('\n Comentario Bloqueado!')
    else:
        comentarios_aprovados.append(f'O Comentario "{texto_comentario}" de {nome_usuario} postado com sucesso!')
        print('\n Comentario postado com sucesso!')

print(f'\n Esses são os comentario: {comentarios_aprovados}')