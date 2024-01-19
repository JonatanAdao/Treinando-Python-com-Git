'''
Exe058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
from time import sleep


computador = randint(1, 10)    #   iniciando variavel computador
contador = 1
rodadas = 5   #     limite de rodadas

print(computador)

jogador = int(input('Qual o numero que pensei ? '))     #   iniciando variavel jogador 
while computador != jogador:
    print('VERIFICANDO ...')
    sleep(2)
    print('Nao foi esse.')
    contador += 1
    
    if jogador > computador:
        print('É menos')
    else:
        print('É mais')
    
    rodadas -= 1
    jogador = int(input('Que numero eu pensei ? '))
   
    if computador == jogador:
        print('VERIFICANDO ...')
        sleep(2)
        print(f'Parabéns vc acertou na {contador}° vez.')
        print(f'Parabéns vc acertou na {rodadas}° rodada.')

    if rodadas == 0:
        print('Você chegou ao limite de rodadas ')
        break



print('FIM DO JOGO')