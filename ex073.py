'''
Ex 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
 Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''
#   Texto cabeçalho.
print('=='*20)
print('{:-^40}'.format('TABELA DO CAMPIONATO BRASILEIRO'))
print('=='*20)
 
#  Passo 1: Criando tupla de tabela do brasileiro.
timesDoCampionato = ('Palmeiras', 'Gremio', 'Atletico', 'Flamengo', 'Botafogo',
                     'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza',
                     'Sao Paulo', 'Cuiaba', 'Corinthians', 'Cruzeiro', 'Vasco',
                     'Bahia', 'Santos', 'Goias', 'Coritiba', 'America')
print('A lista de time são')
for t in timesDoCampionato:
   print(t)
print('=='*20)

#   Passo 2: Mostrando os primeiro 5 colocados...
print(f'Os 5 primeiros colocados do Campionato Brasileiro são: {timesDoCampionato[0:5]}')
print('=='*20)

#   Passo 3: Mostrando os 4 ultimos colocados...
print(f'Os 4 Ultimos colocados do campionato Brasileiro são: {timesDoCampionato[-4:]}')
print('=='*20)

#   Passo 4: Mostrando tabela em ordem alfabetica.
print('A tabela em ordem alfabetica sera assim:')
print(sorted(timesDoCampionato))
print('=='*20)
#   Passo 5: Pegando posiçao de um time.
time = input('Escreva o nome de seu time e fique sabendo a posição dele em nossa tabela: ').strip().title()
if time not in timesDoCampionato:
    print(f'Este time {time} não esta em nosso Campionato')
else:
    print(f'Seu time é {time} e ele se encontra na posição {timesDoCampionato.index(time)+1}° lugar de nossa tabela.')












