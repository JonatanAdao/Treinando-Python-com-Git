''' Desenvolva um programa que leia o NOME , IDADE e SEXO de 4 PESSOAS. 
No final do programa, mostre: a MÉDIA DE DO GRUPO, qual é o nome do homem mais velho e 
quantas mulheres têm menos de 20 anos.'''

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
menorIdadeMulher = 0
nomeNova = ''
posição = 0
# Desenvolva um programa que leia o NOME , IDADE e SEXO de 4 PESSOAS
for pessoa in range(1, 5):
    print(f'_____{pessoa}° pessoa_____')
    nome = str(input('Qual seu Nome? ')).strip()
    idade =  int(input('Qual sua Idade? '))
    sexo = str(input('Indique seu Sexo: [M/F]'))
    somaIdade += idade      #   soma da idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
        posição = pessoa
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
        posição += pessoa
    if sexo in 'Ff' and idade < 20:
        menorIdadeMulher += idade
        nomeNova = nome
        posição += pessoa
        
mediaIdade = somaIdade / 4
print(f'A media da idae do grupo é de {mediaIdade} anos .')
print(f'O Homem mais velho tem {maiorIdadeHomem} e seu nome é {nomeVelho} ')
print (f'A mulher mais nova tem {menorIdadeMulher} e seu nome é {nomeNova} ')


