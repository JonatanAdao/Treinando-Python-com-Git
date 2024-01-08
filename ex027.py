print("""
Ex 027: Faça um programa que leia o nome completo de uma pessoa,
      > mostrando em seguida o primeiro e último nome separadamente.
 """)

nome = str(input('Digite seu nome completo. ')).strip().split()
print(f'O seu primeiro nome é: \n{nome[0]}')
print(f'Seu ultimo nome é: \n{nome[-1]}')
