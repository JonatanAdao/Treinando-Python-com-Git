'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
numero = list()

while True:  
    #   Verificação  se é um numero 
    n =input('Digite um numero: ')
    while  n.isnumeric() == False:
        print('Somente Numeros.')
        n =input('Digite um numero: ')
    n = int(n)
    #   Verificação se o numero esta na lista e esta duplicado
    if n not in numero:
        numero.append(n)
        print('Numero adicionado com sucesso...')
    else:
        print('Numero Duplicado. Não será adicionado...')

    resposta = str(input('Deseja continuar ?[S/N]')).upper().strip()[0]
    #   condição de parada
    if resposta in 'N':
        print('Finalizando')
        break
    #   Verificação  de SIM ou NÂO / S ou N
    while resposta != 'S' and 'N':
        print('Opção Invalida')
        resposta = str(input('Deseja continuar ?[S/N]')).upper().strip()[0]
  
print('-='*40)
numero.sort()
print(f'A sequencio de numeros digitados são: {numero}')