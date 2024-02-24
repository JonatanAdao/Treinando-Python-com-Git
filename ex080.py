'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

#   Lista vazia 
lista = []
#    contagem de 5 usuarios
for c in range(5):
    n = int(input('Digite um numero: '))
#    condição onde o usuario é o primeiro ou o ultimo das lista
    if c == 0 or n > lista[-1] :
        lista.append(n)
        print('Adcionado na ultima posição...')  
#  condição onde aponta a posição do numero na lista         
    else :
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adcionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista} .')
print('fim')