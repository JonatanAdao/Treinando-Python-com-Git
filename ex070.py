'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

totgasto = cont = maisBarato = totMil = 0
barato = ' '
print('-='*20)
print('{:-^40}'.format(' LOJA KI BARATO '))
print('-='*20)

while True:
    nomeProduto = str(input('Qual é onome do Produto?: '))
    precoProduto = float(input('Digite o Preço do Produto: R$ '))
    print('--'*20)
    totgasto += precoProduto
    cont += 1 
    if precoProduto > 1000:
        totMil += 1
    if cont == 1:
        maisBarato =  precoProduto
        barato = nomeProduto
    if precoProduto < maisBarato:
        maisBarato = precoProduto
        barato = nomeProduto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        print('--'*20)
    if resp == 'N':
        print('FINALIZANDO')
        print('--'*20)
        break
print(f'''O total de produtos foi {cont}.
O mais barato foi {barato} no valor de {maisBarato}.
O valor gasto no total foi {totgasto}
E tem {totMil} a cima de 1000 reais.''')