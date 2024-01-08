"""
    Praticado
nome=input('Qual é seu nome?')
idade=input('Qual é sua idade?')
peso=input('Qual é o seu peso?')
print(nome,idade,peso)
"""

#   Exercícios 2, 3, 4.
#   2- Crie um script python que leia e mostre uma mensagen com boas viodas.

print('Exercício 002')
nome=input('Qual é sei nome?')
print(f'Olá, {nome} é um prazer te conhecer.')

#   3- Crie um script python que leia e mostre uma mensagem que mostre dia mes e ano informado.

print('Exercício 003')
dia=input('Qual foi o dia que vc nasceu?')
mes=input('Qual foi o mês em que vc nasceu?')
ano=int (input('Qual o nao em que vc nasceu?'))
idade= 2023-ano
print(f'Você nasceu no dia {dia} no mês {mes} no ano de {ano}')
print(f'Você tem {idade} de idade, correto? ')

#   4- Crie um scrtipt que some dois numeros.

print('Exercício 004')
n1=int(input('Digite um número'))
n2=int(input('Digite outro número'))
st=n1 + n2
print(f'A soma de {n1} + {n2} é = {st}')

