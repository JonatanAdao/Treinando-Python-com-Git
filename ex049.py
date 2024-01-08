print(''' 
Ex049: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
    ''')
n= int(input('Digite o numero da tabuada que vc dejesa ver: '))
for c in range(1, 11):
    print(f'{n} X {c:2} = {(n*c):2}')
print('fim')
