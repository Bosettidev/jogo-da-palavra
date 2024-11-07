
import os
import random

def inicioDoJogo():
    os.system('cls')
    list =[]
    entrada = input('digite uma palavra (nao temos verba para poder digitar numeros): ')
    list.append(entrada)

    while entrada != 'parar':
        print('parar para cancelar')
        entrada = input('digite uma palavra: ')
        if entrada != 'parar':
            list.append(entrada)
        else:
            break
    
    os.system('cls')
    
    print('o computador vai sortear uma dessas palavras tente adivinhar entes de 5 tentativas !!')
    print(f'voce digitou: {list}. tente acertar a palavra agora')

    compTry = random.choice(list)
    
    ajuda = f'{list}'
    
    while entrada != compTry:
        nTentPlayer = 1
        entrada = input('tente acertar: ')
        if entrada != compTry:
            print('voce errou tente de novo. se voce quer saber quais palavras voce falou digite "ajuda" \n')
            nTentPlayer += 1
            entrada = input('tente de novo: ')
            
        if entrada == 'ajuda':
            print(ajuda)

    os.system('cls')
    print(f'PARABENS VOCE ACERTOU A PALAVRA ERA {compTry} !!!')
    print(f'voce fez {nTentPlayer} tentativas')

inicioDoJogo()

def jogarDeNovo():

    jgDNovo = input('voce quer jogar de novo ?? ')

    if jgDNovo == 'sim':
        inicioDoJogo()
    else:
        os.system('cls')
        print('obrigado por jogar')

jogarDeNovo()
