#   EX).:008> Escreva um programa que leia um valor em metros e mostre o valor convertido em centimetros e milimetros. 

m=int(input('Digite um valor. '))
print(f'O valor digitado em metros foi {m}.')
cen=m/100
print(f'{m} metros convertido para cetimetros é de {cen}')
mil=m/1000
print(f'{m} metros convertido em milimetros é de {mil}')