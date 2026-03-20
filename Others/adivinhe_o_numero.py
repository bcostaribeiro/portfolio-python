print( '\n ###### TESTANDO JOGO DE ADIVINHAÇÃO #### \n ')

adivinhado=42
digitado=0

while digitado != adivinhado:
    digitado= int(input('\n Digite o numero dourado: '))

    if digitado > adivinhado:
        print('\n O numero dourado é MENOR!')  
    if digitado < adivinhado:
        print('\n O numero dourado é MAIOR!')

print('\n ACERTOU MIZERAVI!!! \n')
