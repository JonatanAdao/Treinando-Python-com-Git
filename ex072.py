'''
Ex 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeroExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeral = int(input('Digite um valor entre 0 e 20: '))
while numeral < 0 or numeral > 20:
    numeral = int(input('Digite um valor entre 0 e 20: '))
else:
    print(f'Você digitou o numero {numeroExtenso[numeral]}')

