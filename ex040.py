print('''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior:       
''')
nota1 = float(input('Informe nota: '))
nota2 = float(input('Informe nota: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('REPROVADO ')
    print(f'Sua media foi de {media}')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
    print(f'Sua media foi de {media}')
elif media >= 7.0:
    print('APROVADO')
    print(f'Sua media foi de {media}')