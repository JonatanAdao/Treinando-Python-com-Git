print('''
Ex048:Faça um programa que calcule a soma entre todos os números que são múltiplos de três
 e que se encontram no intervalo de 1 até 500.''')
soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0 :
        cont = cont + 1 # ou cont(contador)+= 1
        soma = soma + c # ou soma+=c
print(f'A soma entre todos os {cont} valores multiplos de 3 é igual a {soma}')
print ('fim')