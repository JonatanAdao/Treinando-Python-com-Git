"""Ex 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
# Passo 1 >> Leia o ano de nascimento de um jovem 
anoNasc = int(input('Qual o seu ANO de NASCIMENTO? '))

# Passo 2 >>  informar acordo com a sua idade 
anoAtual = date.today().year 
idade = (anoAtual - anoNasc)
print('Quem nasceu no ano de {} tem {} anos, pois estamos no ano de {}.'.format(anoNasc, idade, anoAtual))

# Passo 3 >> se ele ainda vai se alistar ao serviço militar
if idade <18 :
    saldo = 18 - idade
    ano = anoAtual + saldo
    print('Você ainda nao tem 18 anos.')
    print('Ainda falta {} anos vc se alistara no ano de {}'.format(saldo, ano))

# Passo 4 >> se é a hora exata de se alistar
elif idade == 18 :
    print('Você  tem que se alistar IMEDIATAMENTE.')
    
# Passo 5 >> se já passou do tempo do alistamento
elif idade > 18 :
    saldo = idade - 18
    ano = anoAtual - saldo
    print(f'Você ja deveria ter se alistado a {ano} anos')
    print( 'Ha {} anos atras em {}'.format(saldo, ano))
    
print('FIM')