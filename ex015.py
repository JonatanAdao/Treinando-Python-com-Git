"""
EX.: 015 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
km = float(input('Quantos km foram percorido? '))
print('Foream percorrido {}km.'.format(km))
print('-' *40)
dias = int(input('Por quantos dias fou ultilizado? ' ))
print('Foi ultilizado por {} dias.'.format(dias))
print('-' *40)
valor = (km * 0.15)+(dias * 60)
print('valor total a ser pago é de:R${:.2f}'.format(valor))
