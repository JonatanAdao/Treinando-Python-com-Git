"""
Ex 038:Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
>> O primeiro valor é maior
>> O segundo valor é maio
>> Não existe valor maior, os dois são iguais
"""
# Pedir retorno do usuario.
num1 = int(input('Digite um número. '))
num2 = int(input('Digite outro número. '))
print( num1, num2 )

# Logica para coparação de números.
if num1 > num2:
    print('O primeiro número é maior que o segundo número.')
elif num1 < num2:
    print('O segundo número é maior que o primeiro número.')
else:
    print('Não existe valor maior, os número são iguais.')
print('FIM')