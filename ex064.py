''' 
Tratando vários valores v1.0
'''
n = int(input('Digite um número e [ 999 para PARAR ]: '))
total = 0
c = 0
fim = 999
while n != fim:   
    total += n 
    c += 1    
    n = int(input('Digite um numero e [ 999 para PARAR ] : '))
print(f'foi digitado {c} números.')
print(f'O total dos números digitados foram de {total}.')