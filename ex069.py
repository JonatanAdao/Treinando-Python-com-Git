'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada. 
O programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
print('='*20)
print('  Analize de dados')
print('='*20)

q_pessoa = 0        #  q_pessoa => QUANTIDADE DE PESSOAS.
tot18 = toth = totm = 0

while True:
    i = int(input('Informe sua idade: '))    # i => IDADE.
    s = ' '     # s => SEXO
    while s not in 'MF':
        s = str(input('SEXO [M/F]: ')).strip().upper()[0]
    print('-'*20) 

    if i >= 18:
        tot18 += 1
    if s == 'M':
        toth += 1
    if s == 'F' and i < 20:
        totm += 1
    q_pessoa += 1

    p = ' '
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-'*20) 
#   condiçõa de parada.
    if p == 'N':
        print('FINALIZANDO')
        break

print('Programa encerrado')
print(f'''Ao todo tem {q_pessoa} pessoas cadastradas.
E {tot18} maiores de 18 anos.
E {totm} menores de 20 anos.''')