'''
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder.
Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
v = 0
rodada = 0
while True:
    jogador = int(input('Digite um valor: '))
    cpu = randint(0, 10)
    total = cpu + jogador
    tipo = ' ' 
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar.[P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {cpu}. O total foi de total {total}.')
    print ('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if 'P' == tipo:
        if total % 2 == 0:
            print('JOGADOR VENCEU')
            v += 1
        else:
            print('JOGADOR PERDEU')
            break
    rodada += 1
    if 'I' == tipo:
        if total % 2 == 1:
            print('JOGADOR VENCEU')
            v += 1
        else:
            print('JOGADOR PERDEU')
            break
    rodada += 1
print(f'Você venceu {v} vezes.')
print(f'Você perdeu depois de {rodada} rodadas')
