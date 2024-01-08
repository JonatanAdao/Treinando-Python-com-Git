print('''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
''')
from time import sleep
from datetime import date
ano = date.today().year

nascData = int(input('Imforme o ano de nascimento: '))
idade = ano - nascData
print(nascData)
if idade <= 9:
    print(f'VC tem {idade} idade.Sua categiria é')
    tempo = sleep(2)
    print('MIRRIN')
elif idade <= 14 and idade > 9:
    print(f'VC tem {idade} idade.Sua categiria é')
    tempo = sleep(2)
    print('INFANTIL')
elif idade <= 19  and idade > 14:
    print(f'VC tem {idade} idade.Sua categiria é')
    tempo = sleep(2)
    print('JÚNIOR')
elif idade <= 25 and idade > 19:
    print(f'VC tem {idade} idade.Sua categiria é')
    tempo = sleep(2)
    print('SÊNIOR')
elif idade > 25:
    print(f'VC tem {idade} idade.Sua categiria é')
    tempo = sleep(2)
    print(' MASTER')
