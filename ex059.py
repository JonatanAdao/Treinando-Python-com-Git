'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep

escolha = 0
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
print('=-='*10)

while escolha != 5:    
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa   ''')
    escolha = int(input('Qual é sua escolha? '))

    if escolha == 1:
        print(f'Você escolheu {escolha} soma.')
        sleep(1)
        print(valor1 + valor2)
        print('=-='*10)
    
    if escolha == 2:
        print(f'Você escolheu {escolha} multiplicação.')
        sleep(1)
        print(valor1 * valor2)
        print('=-='*10)

    if escolha == 3 :
        print(f'Você escolheu {escolha}. Vamos mostra o maior valor')
        sleep(1)
        if valor1 > valor2:
            print(valor1)
            print('=-='*10)
        elif valor1 == valor2:
            print('Valores iguais')
            print('=-='*10)
        else:
            print(valor2)
            print('=-='*10)
    
    if escolha == 4 :
        print(f'Você escolheu {escolha}.')
        print('Informe novos valores.')
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
        print('=-='*10)
    if escolha == 0 or escolha > 5:
        print(f'Você escolheu {escolha}.')
        print('Escolha Invalida') 
        print('=-='*10)
    if escolha == 5:
        print(f'Você escolheu {escolha}.')
        print('FINALIZANDO...')
        
        for c in range(3, -1, -1):
            print(c)
            sleep(0.5)

print('Fim do Programa! Volte Sempre!')

