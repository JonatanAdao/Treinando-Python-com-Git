print( """
Ex 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
""" )

n1=int(input('Digite um número. '))
n2=int(input('Digite outro número. '))
n3=int(input('Digite mas um número. '))
print(n1, n2, n3)
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior :
    maior = n3
print(f'O {maior} é maior')

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O {menor} é menor')