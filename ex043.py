print('''Ex 043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida''')

peso = float(input('Informe peso: '))
altura = float (input('Imfome altura: '))
imc = peso / (altura**2)
print('Seu Indice de Massa Corporal é de: {:.2f}'.format(imc), end =' ')
if imc <= 18.5:
    print('Faixa de Abaixo do Peso. ')
elif imc > 18.5 and imc <= 25.0:
    print('Faixa de Peso Ideal. ')
elif imc > 25.0 and imc <= 30.0:
    print('Faixa de Sobrepeso. ')
elif imc > 30.0 and imc <= 40.0:
    print('Faixa de  Obesidade')
else:
    print('Faixa de Obesidade Morbida')
print('Obrigado e Boa saúde ')
