print("""
Ex025: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
      """)
nome = str(input('Digite seu nome. ')).strip().lower()
print(len(nome.replace(' ','')))
print('silva' in nome)

