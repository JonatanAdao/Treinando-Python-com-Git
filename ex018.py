import math
"""
Ex 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
angulo = int(input('Digite o angulo dasejado: '))
print(angulo,'°')
print('-' * 40)
rad =  math.radians(angulo)
print(rad)
print('-' * 40)
seno = math.sin(rad)
coseno = math.cos(rad)
tangente = math.tan(rad)
print(f'{seno:.2f} - {coseno:.2f} - {tangente:.2f}')
print('-' * 40)

