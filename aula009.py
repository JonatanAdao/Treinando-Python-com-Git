print("""
Nessa aula, vamos aprender operações com String no Python.\nAs principais operações que vamos aprender são o Fatiamento de String,\nAnálise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
""")
print('='*99)
#   FATIAMENTO
frase = 'Curso em Video Python'
print(frase)
print('\nFatiamento individial\n')
print(frase[9]) # retorna = V
print('\nFatiamento de interval\n')
print(frase[9:14]) # retorna = Video.
print(frase[9:21]) # retorna = Video Python.
print(frase[9:21:2]) # retorna = VdoPto >> 1° instante inicio da contagem, 2°instante indica onde terminara a contagem e 3°instante intervalo da contagem.
print(frase[:5]) # retorna = Curso >> Nao existindo o 1° instante, inciará do caracter 0 até o 2° instante indicado.
print(frase[15:]) # retorna = Python >> Na existencia só do 1° instante, iniciara do indicado até o final da string.
print(frase[9::3]) # retorna = VePh >> Na não existencia do 2° instante, ocorrera a contagem do caracter informado ate o fim da string com o 3° indicado.
print('\nAnalise\n')
print(len(frase)) # retorna a contagem ou conta a string.
print(frase.count('o')) # retorna quantas vezes o caracter indicado aparece. 
print(frase.count('o',0,14)) # retorna a contagem ja com fatiamaento.
print(frase.find('deo')) # retorna em que momento começa o momento indicado.
print(frase.find('Android')) # retorna o valor -1. Pois a string indicada é inexistente.
print('Curso' in frase) # retorna True, caso existencis da string. 
print('\nTransfomação\n')
print(frase.replace('Python', 'Android')) # retorna ou substitui a 1°string pela 2°.
print(frase.upper()) # Passa todos os caracteres da string indicada para MAIUSCOLAS ou caixa alta.
print(frase.lower()) # Passa todos os caracteres da string indicada para MINUSCULAS ou caixa baixa.
print(frase.capitalize()) # Passa o 1° Primeiro caracter da string para caixa alta e os outros caracteres para caixa baixa. 
print(frase.title()) # Passa todos os 1° caracteres da string para caixa alta.
print(frase.strip()) #  Remove espaços inutes.
print(frase.rstrip()) # Remove espaços inutes da direita.
print(frase.lstrip()) # remove espaços inutes da esquerda.
print('\nDivisao de Strings\n')
print(frase.split()) # Retorna fazendo uma lista da string.
print('/'.join(frase)) # Retorna a junção das strings pelo caracter indicado.
