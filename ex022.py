print("""
Ex 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
  *  O nome com todas as letras maiúsculas e minúsculas.
  *  Quantas letras ao todo (sem considerar espaços).
  *  Quantas letras tem o primeiro nome.""")
print('=*' *51)
nomeCompleto = str(input('Digite seu nome completo. '))
print(nomeCompleto)
print('=' *100)
print('\nSeu nome em letras MAIÙSCULAS é: \n{}'.format( nomeCompleto.upper()))
print('=' *100)
nomeCompleto2 = nomeCompleto.upper()
print('\nSEU nome com letras minúsculas\n{}'.format( nomeCompleto2.lower()))
print('=' *100)
print('Seu nome possui {} letras'.format( len(nomeCompleto.replace(' ',''))))
print('=' *100)
nomeCompleto = nomeCompleto.split()
print(f'Seu primeiro nome é:{nomeCompleto[0]}\nE tem {len(nomeCompleto[0])} letras')