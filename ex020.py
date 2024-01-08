import random
print("""
Ex.: 020: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
""")
print('=' *99)
aluno1 = str(input('Digite o nome do aluno. '))
aluno2 = 'Flavio'
aluno3 = 'Gustavo'
aluno4 = 'Hugo'
aluno5 = 'Igor'
alunos =[aluno1, aluno2, aluno3, aluno4, aluno5 ]
print(alunos)
print('-' * 40)
random.shuffle(alunos)
print(alunos)