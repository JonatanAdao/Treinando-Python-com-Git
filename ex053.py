print('Escreva um codigo que diga se uma palavra é palindra  ')

frase = str(input('Digite uma frase e verifique se ela é um palindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(palavras)
print(junto)
for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]
if inverso == junto:
    print(f' Sim esta frase é um palíndromo.E a frase foi {inverso} {frase}.')
else:
    print(f' Não, Esta frase não é um palíndromo E a frase foi {inverso} {frase}.')
