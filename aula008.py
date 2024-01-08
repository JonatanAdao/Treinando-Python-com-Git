import random
from emoji import emojize
from math import sqrt
"""
Aula 8:vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas 
utilizando módulos built-in e módulos externos, oferecidos no Pypi.
"""

num =  random.randint(1, 20)

raiz= sqrt(num)
print(num, raiz)
ale = random.randint(1, 10)
print(ale)
print(emojize('Python é o 👌'))