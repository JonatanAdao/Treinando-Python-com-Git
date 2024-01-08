"""Ex036:
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    >  Pergunte o valor da casa, >o salário do comprador e em > quantos anos ele vai pagar. 
    A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.\n"""

print('=-'*30)
            # logica de  valores e tempo
valorCasa = float(input('Informe valor do Imovel: '))
print(valorCasa)
valorSalario = float(input('Informe valor do salario: '))
print(valorSalario)
anos = int(input('Periodo  de pagamento: '))*12
print('=-'*30)

import time             #  <== importação de biblioteca
                        #  Formação das condições
if (valorCasa/anos) > (valorSalario * 30/100):
    print('ANALIZANDO ...')
    time.sleep(3)
    print( 'Emprestimo Negado 👎 ')
    print('Sinto Muito')
else:
    print('ANALIZANDO ...')
    time.sleep(3)
    print('Emprestimo Aprovado 👍')
    print('Vamos fechar o contrato.')

print('Para pagar ')

