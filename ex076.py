'''
 Ex076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

print('--'*20)
print('{:^40}'.format('TABELA DE PREÇO'))
print('--'*20)
tabela = ('Lápis', 1,
        'lapiseira', 2.99,
        'Borracha', 1.59,
        'Apontador', 2.99,
        'Canetinhas', 37.78,
        'Lápis de cor', 18.90,
        'Marca-texto', 13.90,
        'Corretivo', 7.83,
        'Cola escolar',6.99)
for p in range(0,len(tabela)):
    if p % 2 == 0:
        print(f'{tabela[p]:.<30}', end=' ')
    else:
        print(f'R$ {tabela[p]:>5.2f}')