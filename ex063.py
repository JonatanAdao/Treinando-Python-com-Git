'''Ex063: Sequênçia de fibonacci'''

anterior = 0
atual = 1
proximo = 1
contador = 0
quan_num = int(input('Em qual termo da sequência gostaria de terminar?: '))
print(f'Você  escolheu {quan_num} termos.')
while contador <= quan_num:
    print(anterior, end=' ')
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    contador += 1
print('\nFIM')