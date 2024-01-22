'''
Ex 060 : Crie um programa que leia um numero qualquer e mostre seu fatorial
'''

n = int(input('Informe um número: '))
c = n
f = 1
print(f'Calulando fatorial de {n}')
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c >1 else '=', end=' ')
    f *= c
    c -= 1
print(f'{f}')