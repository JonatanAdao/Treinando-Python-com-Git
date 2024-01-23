"""
Ex 062: Melhorando ex061  
"""

from time import sleep

print('Gerador de P.A')
print('-='*10)

primeiro = int(input('Primeiro termor P.A: '))
razão = int(input('Indique a Razão da P.A: '))
print('-='*10)
inter = 0
cont = 1
maisTermos = 10
while maisTermos != 0:
    inter = inter + maisTermos
    while cont <= inter:
        print(primeiro, end=' ')
        primeiro += razão
        cont+=1
    print('\nPAUSA')
    maisTermos = int(input('Mais quantos termos gostaria de mostrar? '))
print('Finalizando...')
sleep(2)
print(f'O total de termos foi {inter}')
print('')