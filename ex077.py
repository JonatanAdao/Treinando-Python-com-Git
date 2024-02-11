'''
Exe 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
#   Definindo tupla com as palavras.
palavras = ('ALUNO','ESTUDANTE','PROGRAMAÇAO',
            'APRENDENDO','LINGUAGEM','PYTHON')

#   Iterando  sobre cada palavra em tupla 
for palavra in palavras:
    print(f'\nNa palavra {palavra} contem as vogais',end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')

