import math
"""
Ex.: 017 Faça um programa que leia o comprimento do cateto oposto
 e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

catetoOposto = float(input('Digite o valor do Cateto Oposto: '))
print(catetoOposto)
print('-'*40)

catetoAdjacente = float(input('Digite o valor do Cateto Adjacente: '))
print(catetoAdjacente)
print('-'*40)

#hipotenusa = math.sqrt( (catetoOposto*catetoOposto) + (catetoAdjacente*catetoAdjacente)) 
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)      # Outra forma de cacular hipotenusa
print(f'O comprimento da hipotenusa é de {hipotenusa:.2f}')
print('-'*40)