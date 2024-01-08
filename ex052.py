print('Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.')
# 1 lendo número
num = int(input('Digite um número. '))
tot =0
for n in range ( 1, num+1 ):
    if num % n == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
        print(f'{n} ', end='')
        print(f'\n\033[m O número digitado foi {num} e foi dividido {tot}.')
if tot == 2:
    print ('Este número é primo.'.upper())
else:
    print('ESTE NÚMERO NÃO É PRIMO')
    