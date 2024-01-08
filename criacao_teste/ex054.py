'''Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

# Importando biblioteca Date DateTime
from datetime import date
total_maior = 0
total_menor = 0
ano_atual= date.today().year
for pessoa in range(1, 8):
    nascimento = int(input(f'Qual o ano de nascimento {pessoa}° pessoa ? '))
    idade = ano_atual - nascimento
    if idade < 18:
        total_menor += 1
       
    else:
        total_maior += 1
        
print(f'Ao todo tivemos {total_maior} é maior de idade.')

