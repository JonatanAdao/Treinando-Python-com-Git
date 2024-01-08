# EX.:013> Faça um programa que leia um salario de um funcionario e acrescete um aumento de 15%. 

salario=float(input('Digite o valor do salario. '))
acrescimo=(salario/100)*15
novoSalario=salario + acrescimo 
print(f'Seu salario é de R$ {salario:.2f} e terá um aumento de R$ {acrescimo:.2f}\n onde passará a ser de R${novoSalario:.2f} ')
 