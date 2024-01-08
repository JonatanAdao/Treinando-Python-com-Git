from random import randint

print(""" Ex 030:  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. """)
cpu = randint(0,10)
jogado = int(input('Faça sua escolha, (1) para impar ou (2) para par: '))

if jogado == 1:
    print ('Você escolheu IMPAR.')
    num = int(input('Digite um número: '))
    # print(num, cpu, (num + cpu))
    resultado = (cpu + num)%2
    # print(resultado)
    if resultado  == 0:
        print('Você perdeu.')
        print('Deu PAR.')
    else:
        print('Você venceu.')
        print('Deu IMPAR.')
else:
    print ('Você escolheu PAR.')
    num = int(input('Digite um número: '))
    # print(num, cpu, (num + cpu))
    resultado = (cpu + num)%2
    # print(resultado)
    if resultado  == 1:
        print('Você venceu.')
        print('Deu IMPAR.')     
    else:
        print('Você perdeu.')
        print('Deu PAR.')
print ('FIM')