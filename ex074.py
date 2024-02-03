        # Detalhes Do Exercicio
'''
Ex 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
# Passo 1: Importa modulos que gerem numeros aliatorios
import random

# Passo 2: Criar programa que gere 5 numeros aliatorio mostre a listagem deles
numeros = (0,1,2,3,4,5,6,7,8,9)
numeroMistos = random.choices(numeros, k=5)
print(f'Os numeros gerados são: {numeroMistos}')

# Passo 3: Indicação de maior e menor
print(f'O maior valor dos numeros gerado foi :{max(numeroMistos)}')
print(f'O menor valor dos numeros gerado foi: {min(numeroMistos)}')


