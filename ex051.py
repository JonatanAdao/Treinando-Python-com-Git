print('progreção aritimetica')

seq = int(input('Digite o valor da Sequencia: '))
razao = int(input('Digite valor da Razão: '))
decimo = seq + (10 - 1 ) * razao
for c in range (seq, decimo + razao, razao):
    print(f'{c}->', end=' ')
print('Acabou')

