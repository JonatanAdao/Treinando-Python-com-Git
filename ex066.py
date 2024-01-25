''' 
Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

soma = 0
cont = 0
while True:  
    print('-='*20)  
    num = int(input('Digite um número: '))
    if num == 999:
        print('-='*20) 
        print('FINALIZANDO')
        print('-='*20) 
        break 
    else:
        soma += num
        cont += 1
print(f'foi digitado {cont} números. Soma entre todos os termos foi de {soma}.')
print('FIM')