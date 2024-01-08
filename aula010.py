print("""
Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
      """)
resposta = int(input('Qual exemplo deseja execultar? 1 ou 2: '))
print(resposta)

if resposta == 1:
    print('-' *100)

    print(('Prmeiro exemplo.'))
    tempo = int(input('Quantos anos tem seu carro '))
    if tempo <= 3:
        print('Seu carro é Novo.')
    else:
        print('seu carro é Semi novo.')
    print('FIM')
     
else:
    print('-'*100)
    
    print('Seungundo exemplo.')
    nome = str(input('Qual é seu nome. ')).upper()
    if nome == 'ADAO':
        print('Você esta na lista')
    else:
        print('Você não esta na lista')
    print('FIM')
    print('-'*100)