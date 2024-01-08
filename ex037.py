""" 
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
>> 1 para binário, 
>> 2 para octal e 
>> 3 para hexadecimal."""

# Escreva um número inteiro qualquer
numero = int(input('Digite um numero inteiro. '))
print(numero)
# peça para o usuário escolher qual será a base de conversão
opçao = int(input('''Escolher qual será a base de conversão.
[1] para binário.
[2] para octal.
[3] para hexadecimal.  '''))
    
        # CONDIÇÕES
if opçao == 1:
    print('O {} convertido para Binario {}'.format(numero, bin(numero)[2:]))
elif opçao == 2:
    print('O {} convertido para Octal {}'.format(numero, oct(numero)[2:]))
elif opçao == 3:
    print('O {} convertido para Hexadecimal {}'.format(numero, hex(numero)[2:]))
else:
    print('Número Invalido')
print('FIM')
