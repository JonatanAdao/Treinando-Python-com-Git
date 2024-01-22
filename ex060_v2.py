n = int(input('Informe um número: '))
c = n 
f = 1
print(f'Calculando o fatorial de {n}.')
for c in range(n, 0,-1):
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
print(f)
    