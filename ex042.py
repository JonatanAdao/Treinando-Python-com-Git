print('''Ex 042 Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes''')

r1 = float(input('Informe tamanho da reta: '))
r2 = float(input('Informe tamanho da reta: '))
r3 = float(input('Informe tamanho da reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('COORDENADAS formam TRIANGOLO')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('COORDENADA nao formam um TRIAGULO')
    