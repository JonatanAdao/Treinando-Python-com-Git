r1 = 'S'
n = 0
c = 0
soma = 0
media = 0
maior = 0
menor = 0
while 'S' in r1:
    n = int(input('Digite um valor: '))
    c += 1
    soma += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    media = soma / c
    r1 = str(input('Que continuar [S/N]: ')).upper()
    
print(f'''Você digitou {c} números.
A Média dos números digitados foram de {media}.
O Maior valor foi {maior} e o Menor foi {menor}.''')
print('FIM')