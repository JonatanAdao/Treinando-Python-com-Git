print(""" O Curso de Python está de volta no seu Mundo 2 e vai falar sobre Estruturas de Controle da linguagem: 
if.. elif.. else, for e while.""")

nome = str(input('Qual seu nome ? ')).capitalize()
if nome == 'Jonatan':
    print('Que nome lindo.')
elif nome in 'Vitor Tales Tarciso Hugo':
    print('Seu nome é especial.')
elif nome == 'Adao' or 'Alessandra' or 'Marly':
    res=str(input('Você é algun parente do Jonatan ? ')).capitalize()
    if res == 'Sim':
        print('É um prazer conhece-lo.👍')
    else:
        print(' Ta ok.👌')

print('Até a proxima  👋!!!!')
