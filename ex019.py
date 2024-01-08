from random import choice
print("""
Ex 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
 Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
""")
print('='*99)

nome1 = str(input('Digite nome do aluno. '))
nome2 = 'Bernado'
nome3 = 'Carlos' 
nome4 = 'David'
nome5 = 'Erike'
listaAluno = [ nome1, nome2, nome3, nome4, nome5 ]
# print( listaAluno)
print('-'*40)
sorteio = choice(listaAluno)
print( sorteio )
print('-' *40)