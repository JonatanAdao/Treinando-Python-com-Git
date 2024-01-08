"""
        Cores no terminal

Nessa aula,
vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. 
Veja como utilizar o código \033[m com todas as suas principais possibilidades. 
        Tabel Cores:
preto = ' \033 [30m '
vermelho = ' \033 [31m ' 
verde = ' \033 [32m '
amarelo = ' \033 [33m '  
azul = ' \033 [34m '
magenta = ' \033 [35m ' 
ciano = ' \033 [36m ' 
branco = ' \033 [37m '
restaura  cor  original = ' \033 [0;0m '
        
        Tabela Cores Fundos:
  
fundo  preto = ' \033 [40m ' 
fundo  vermelho = ' \033 [41m ' 
fundo  verde = ' \033 [42m ' 
fundo  amarelo = ' \033 [43m ' 
fundo  azul = ' \033 [44m ' 
fundo  magenta = ' \033 [45m ' 
fundo  ciano = ' \033 [46m ' 
fundo  branco = ' \033 [47m '


negrito = ' \033 [1m ' 
reverso = ' \033 [2m ' 
underline = ' \033[4m '
 
"""
print('\033[31;4;43m Olá Mundo\033[m')
s = 'prova de python'
print(len(s))