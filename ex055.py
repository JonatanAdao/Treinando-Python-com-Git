''' Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''


maior = 0
menor = 0

for pessoa in range(1, 5):

    peso = float(input(f'{pessoa}° Qual seu peso? '))
    
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é de {maior} kg.' )
print(f'O menor peso é de {menor} Kg.' )

