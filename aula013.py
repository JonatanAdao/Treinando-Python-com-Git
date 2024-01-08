'''
    ESTRUTURA DE LAÇOS COM O "FOR".
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
que é uma estrutura versátil e simples de entender. Por exemplo:
'''
# exemplo 01
for c in range(0, 4):
    print(c)
print('Acabou')
# exemplo 02
for c in range(0,7,2):# contagem com intevalo (pulo) de 2 em 2.
    print(c)
print('Fim')
# exemplo 03
for c in  range(6,0,-1):# contagen de traz para frente.
    print(c)
print('Fim')
# exemplo 04
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('Fim')
# exemplo 05
t = int(input('Digite numero para ver sua tabuada: '))
for c in range(1, 11):
    print(t, c, c*t)
print(' Fim')
# exemplo 06
i = int(input('Inicio: '))
f = int(input('fim:'))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('acabou')
# exemplo 07
s = 0
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    s+= num # É o mesmo que s = s+num
print(f'A soma entre  os valores é igual a {s}')


