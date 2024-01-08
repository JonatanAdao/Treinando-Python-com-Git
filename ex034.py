print("""Ex 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
       Para salários superiores a R$1250,00, calcule um aumento de 10%.
       Para os inferiores ou iguais, o aumento é de 15%.""")

salario = float(input('Informe valor do SALÁRIO R$: '))
print(f'O salário informado  foi R$ {salario:.2f}')
if salario > 1250 :
    aumento = salario + (salario * 10 /100)
    print(f'Seu salario reajustado com mais 10%.\n Valor antigo R$ {salario:.2f}.\nValor novo R$ {aumento:.2f}.')
else:
    aumento = salario + (salario * 15 /100)
    print(f'Seu salário foi reajustado com mais 15%.\n Valor antigo R$ {salario:.2f}.\nvalor novo R$ {aumento:.2f} ')