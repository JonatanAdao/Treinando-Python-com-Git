print('Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.')
from random import randint
from time import sleep

print('\033[31;43m {:=^40}\033[m'.format(' JOKENPÔ'))
itens =('👊 pedra', '🖐️ papel','✌️ tesoura')
cpu = randint(0,2)

jogador = int(input('''ESCOLHA SUA JOGADA:
[0]PEDRA
[1]PAPEL 
[2]TESOURA
'''))

print('-='*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
sleep(1)
print('-='*20)

if cpu == 0:
    if jogador==0:
        print('EMPATE')
    elif jogador ==1:
        print('VITORIA DO JOGADOR')
    elif jogador == 2:
        print('\033[31;43m VITORIA DA CPU\033[m')
    else:
        print('opção invalida')
        print('tente novamente')
elif cpu == 1:
    if jogador == 0:
        print('\033[31;43m VITORIA DA CPU\033[m')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITORIA DO JOGADOR')
    else:
        print('opção invalida')
        print('tente novamente')
elif cpu == 2:
    if jogador == 0:
        print('VITORIA JOGADOR')
    elif jogador == 1:
        print('\033[31;43m VITORIA DA CPU\033[m')
    elif jogador == 2:
        print('EMPATE')

print('-='*20)
print(f'A Escolha da CPU foi {itens[cpu]}')        
print(f'A Escolha do JOGADOR foi {itens[jogador]}')
