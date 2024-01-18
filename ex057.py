
''' Exe057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto. 
'''


sexo =str( input('Informe sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo !='F':
    print('Informação Invalida')
    sexo =str( input('Informe sexo [M/F]: ')).upper().strip()
    if sexo == 'M' or  sexo == 'F':
        print('Sexo cadastrado')

       

