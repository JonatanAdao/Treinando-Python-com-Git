'''
Ex 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print('Gerador de P.A')
print('-='*10)

primeiro = int(input('Primeiro termor P.A: '))
razão = int(input('Indique a Razão da P.A: '))
print('-='*10)
inter = 10
cont = 0
while cont < inter:
        print(primeiro, end=' ')
        primeiro += razão
        cont+=1
print('\nFIM')
