#     EX.:012> Faça um algoritimo que leia um preço de um produto e dê 5% de desconto.

preco=float(input('Digite o preço. '))
print(preco)
desconto=(preco/100)*5
novoPreco=preco-desconto
print(f'O preço é de R$ {preco:.2f},mais com desconto de 5% no  valor de R$ {novoPreco:.2f}.')
