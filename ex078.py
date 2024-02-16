''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

# Lista vazia para salvar numeros  
valores = []
# Incrementado valor  lista de valores
for valor in range(1,6):
    valores.append (int(input(f'Digite um valor {valor}: ')))

# Resultado da lista
print(f'Os valores digitados forem: {valores}')

# Resultado do maior e menor da lista 
print(f'O maior numero digitado foi: {max(valores)}')
# Posição dos maior numero digitado
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'E aparece nas posições {i+1}...', end=' ')
print()
print(f'O menor numero digitado foi: {min(valores)}')
# Posição dos menor numero digitado
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'E aparece nas posiçoes {i+1}...', end=' ')


# print(f'O maior valor da lista é :{valores.index(max(valores))+1}.')
# print(f'O menor valor da lista é :{valores.index(min(valores))+1}.')