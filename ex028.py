from random import randint
from time import sleep

print("""Ex 028: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
     e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
       O programa deverá escrever na tela se o usuário venceu ou perdeu.""")
print('-' *100)
cpu = randint(0, 5)     # cpu escolhendo um numero entre 0 e 5
# print(cpu)
usuario = int(input('Advinhe em que númro estou pensando? '))   #   usuario escolhendo sua resposta
print('VERIFICANDO ....')
sleep(3)
if cpu == usuario:
    print('Você acertou.👍')
else:
    print('Você errou.👎')