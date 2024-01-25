'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
'''
print('-='*20)
print('            TABUADA 3.0v      ')
print('-='*20)


while True:
    num = int(input('Qual o número vc quer ver a Tabuada: '))
    print(f'Você escolheu a Tabuada de {num}.')
    print('-='*20)
    
    if num < 0:
        print('SAINDO...')
        break

    for cont in range(1, 11):
        print(f'{num} X {cont} = {num*cont}')
        
print('FIM')