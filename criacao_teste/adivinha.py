import random

# NOMES E ESCOLHA DA CPU
palavras = ['imperatriz', 'Sao luiz', 'paraupebas', 'sao paulo', 'rio de janeiro', 
'niteroi','abacaxi']
print(palavras)
resposta = random.randint(0 , len(palavras)-1)
jogada = 1

#ESTRUTURA DE REPETIÇÃO E SAIDA DO LAÇO
for c in range (1,4):
    tentativa = str(input('\nA divinhe a palavra! ')).strip()

    if palavras[resposta] == tentativa:
        print('\033[31mParabéns!!\033[m')
        break #SAIDA
    else :
        print(f'Palavra errada. Tente de novo. {jogada} Chance ja foi. ')
        jogada +=1

# ANINHAMENTO DE PARABENIZAÇÃO 
if jogada > 3: 
    print(f'Todas suas tentativas acabaram \033[34m{palavras[resposta]}\033[m .')
elif jogada == 2:
    print('Ufa foi por pouco!!! Mais Parabéns!!!  ')
else:
    print('\033[31mParabéns!!\033[m')