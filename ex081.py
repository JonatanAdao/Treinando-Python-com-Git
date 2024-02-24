'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
    A) Quantos números foram digitados.
        B) A lista de valores, ordenada de forma decrescente.
            C) Se o valor 5 foi digitado e está ou não na lista.
'''

listaNumero =[]
while True:
    numeroDigitado = int(input('Digite um numero: '))
    listaNumero.append(numeroDigitado)
    res = input('Deseja continuar? [S/N]:').upper().strip()[0]
    if res in 'S':
        continue
    if res in 'N':
        print('Finalizando agora.')
        print('-=-'*20)
        break
    while res != 'S'and 'N':
        print('OPÇÂO INVALIDA.')
        print('TENTE NOVAMENTE.')
        res = input('Deseja continuar? [S/N]:').upper().strip()[0]
print(f'{len(listaNumero)} numeros digitado na lista.' )
listaNumero.sort()
print(f'Esta é a lista em ordem decrescente : {listaNumero[::-1]}')
print('-=-'*20)
if 5 in listaNumero:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 nao foi encontrado.')
print('-=-'*20)
print('Fim do Programa.')