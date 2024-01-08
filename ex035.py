print("""
Ex 035: Desenvolva um programa que leia o comprimento de três retas
       e diga ao usuário se elas podem ou não formar um triângulo.
      """)

r1=float(input('Digite um número. '))
r2=float(input('Digite outro número. '))
r3=float(input('Digite mas um número. '))

print(r1, r2, r3)   
"""
    minha resolucção

if r1 > r2:  
    maior = r1
    soma = r2 + r3
if r2 > r3:
    maior = r2
    soma = r1 + r3
if r3 > r1 :
    maior = r3
    soma = r1 + r2
if soma > maior:
    print('A medidas formam um triangolo')
else:
    print('As medidas nao formam um triangolo')
"""

 # resolução do curso
if r1< r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('é um triangolo')
else:
    print('nao é um triangolo')