''' Crie um programa que leia /o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

ano_atual = date.today().year
total_maior = 0
total_menor =0
for pessoas in range(1,8):
    ano_nasc = int(input(f'{pessoas}° Em que ano você nasceu? '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print(f'Ha um total de {total_maior} pessoas maiores de idade.')
print(f'E também existe {total_menor} pessoas menores de idade.')