print('=='*20)
print('{:-^40}'.format('Bank EX 071'))
print('=='*20)

valor = int(input('Digite o VALOR que desejado: R$ '))
print(f'O valor solicitado para saque foi de R$ {valor}')
print('--'*20)
valor_total = valor
ced = 100
total_ced = 0
while True:
    if valor_total >= ced:
        valor_total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'O Total de {total_ced} cedulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        total_ced = 0
        if valor_total == 0:
            break
print('=='*20)
print('Volte Sempre ao Bank EX 071')
print('=='*20)

