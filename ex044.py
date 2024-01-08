print('{:=^40}'.format('GERENCIADOR DE COMPRAS'))

valorP = float(input('Informe preço do produto:R$ ')) # variavel para valor do produto
print('Opição de pagamento')
opcaoPg = int(input('[1]- Pagamento À VISTA [2]- pagamento no CARTÂO PARCELADO: '))   # variavel para opção de pagamento
if opcaoPg == 1:
    print('Pagamento À VISTA.')
    print('DINHEIRO, CHEQUE ou CARTÂO?')
    dinCar = int(input('[1]- DINHEIRO/CHEQUE [2]- CARTÂO: '))   # variavel para dinheiro, cheque ou cartão
         #à vista dinheiro/cheque: 10% de desconto
    if dinCar == 1:        
        print('Pagamento em DINHEIRO ou CHEQUE')
        valorN = valorP -((valorP * 10)/100)    # variavel para novo valor do produto
        print(valorN)
        # à vista no cartão: 5% de desconto
    elif dinCar == 2:       
        print('pagamento À VISTA no CARTÃO ')
        valorN =valorP -((valorP * 5)/100)
        print(valorN)

elif opcaoPg == 2:         
    print('Pagamento PARCELADO no CARTÂO.')
    qntParc = int(input('INFORME a QUANTIDADE de PARCELAS?: '))
    if qntParc == 2:    # em até 2x no cartão: preço formal
        print(f'PARCELAMENTO em {qntParc}X')
        print(valorP)
        print(valorP/qntParc)
    elif qntParc > 2:      # 3x ou mais no cartão: 20% de juros
        print(f'PARCELAMENTO em {qntParc}X')
        valorN = valorP +((valorP * 20)/100)
        print(valorN)
        print(valorN/qntParc)
