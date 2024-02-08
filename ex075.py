#   DETALHES DO ARQUIVO 075
'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
valor = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o ultimo valor: ')))
print(f'Os valores digitados foram: {valor}')
print(f'O valor 9 apareceu {valor.count(9)} vezes.')
if 3 in valor:
    print(f'O numero 3 apareceu em {valor.index(3)+1}° lugar. ')
else:
    print('O numero 3 não apareceu entre os numeros digitados')
print(f'Os valores PARES sao: ')
for v in valor:
    if v % 2 == 0:
        print(v, end=' ')
  

