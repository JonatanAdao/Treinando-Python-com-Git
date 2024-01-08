print("""
 Desenvolva um programa que pergunte a distância de uma viagem em Km.
>Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
e R$0,45 parta viagens mais longas.
 """)
viagem = int(input('Qual a distância de sua viagem em Km. '))
if viagem <= 200:
    valor = viagem * 0.50
    print (f'Vc pagara na sua viagem de {viagem} km o valor de {valor:.2f}.')
else:
    valor = viagem * 0.45
    print (f'Vc pagara na sua viagem {viagem} km o valor de {valor:.2f}.')
    