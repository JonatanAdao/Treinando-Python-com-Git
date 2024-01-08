import datetime
# import calendar

print("""
      Ex 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
""") 
ano =int(input('ano '))
if ano == 0:
    ano = datetime.date.today().year
    print(ano)

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Bissexto')
else:
    print('Não é bissexto') 
"""
    SCRIPT SIMPLIFICADO

ano = int(input('Digite o ano desejado? '))
if calendar.isleap(ano):
    print('O ano informado é BISEXTO.')
else:
    print('O ano informado não é BISEXTO.')
"""    