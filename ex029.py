print("""Ex 029: Escreva um programa que leia a velocidade de um carro.
       Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
       A multa vai custar R$7,00 por cada Km acima do limite.
""")
print('=--'*60)
velocidade = int(input('Indique a velocidade do carro? '))
print(f'A velocidade indicada foi de: {velocidade}Km/h')
if velocidade <= 80:
    print('PARABÈNS você esta detro do limites de velocidade.')
    print('VOCÊ NÃO SERÁ MULTADO.')
else:
    multa = (velocidade - 80)*7
    print('INFELIZMENTE você escedeu a limite de velocidade.')
    print('VOCÊ SERÁ MULTADO')
    print(f'Você pagar uma MULTA no valor de R${multa:.2f}')
