print('''
Ex050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
''')
soma1 = 0
cont1 = 0
for c in range(1, 7):
    num1 = int(input(f'Digite {c}° numero: '))
    if num1 % 2 == 0:
        soma1 += num1
        cont1 += 1
print(f'Toatal de numeroa pares foi de {cont1}')
print(f'Todos os numeros pares somam o valor total: {soma1}')
print('fim')

# exemplo 02 Teste de automaçã de numeros
import random
from time import sleep
soma2 = 0
cont2 = 0
for c in range(1, 7):
    num2 = random.randint(1, 100)
    print(num2)
    sleep(0.5)
    if num2 % 2 == 0:
        soma2 += num2
        cont2 += 1
print(f'Total de vezes {cont2} e total de somado {soma2}')