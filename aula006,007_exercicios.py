#   Aula 006 - TIPOS PRIMITIVO.
print("""
  Pricipais tipos primitivos
    int > Indica números inteiros EX.: 1, 4, 7.
    float > Indica números flutuantes ou números reais (separadp por ponto)EX.: 4.5, 3.14, 52.98.
    bool > Indica valores lógico só aceitando dois tipos EX.: True / False
    str >  Sequências de caracteres alfanuméricos (letras, números e/ou símbolos) 
""")
#   Aula 007 - OPERADORES ARITIMÉTICOS 
print("""
        Operador	Operação	Explicação
    (+)	Soma	Realiza a adição dos dois operandos. 5 + 2
    (-)	Subtração	Subtrai o operando da direita do o perando à esquerda 5 - 2
    (*)	Multiplicação	Realiza a multiplicação entre os dois operandos 5 * 2
    (/)	Divisão	Divide o operando à esquerda pelo operando à direita  5 / 2
        Operador	Conceito	Exemplo
    (*) (Multiplicação)	Realiza a multiplicação entre operandos	3 * 4
    (/) (Divisão)	Realiza a divisão entre operandos	10 / 5
    (//) (Divisão inteira)	Realiza a divisão entre operandos e a parte decimal do resultado	10 // 6
    (%) (Módulo)	Retorna o resto da divisão entre operandos	4 % 2
       
        Ordem de Precedência
      1> ()
      2> **
      3> * / // %
      4> + -
""")

#     EX.:005> Faça um programa que leia um número e mostre seu sucessor e seu antecessor.

#     EX.:006> Crie um algoritimo que mostre seu dobro, triplo e ao quadrado.

#     EX.:007> Desenvolva um programa que lêia e calcule a nota de um aluno e mostre sua media.

#     EX).:008> Escreva um programa que leia um valor em metros e mostre o valor convertido em centimetros e milimetros. 

#     EX.:009> Faça um programa que leia um numero e mostre sua tabuada na tela.

#     EX.:010> Faça um programa leia quanto dinhero a pessoa tem na carteira e converta em dolares.

#     EX.:011> Faça um program que leia a altura e largura de uma parede em metros, 
#     calcule sua area e a quantidade de de tinta para pinta-la. Sabendo que cada litro de tinta pinta uma area de 2m².
   
#     EX.:012> Faça um algoritimo que leia um preço de um produto e dê 5% de desconto.

  #     EX.:013> Faça um programa que leia um salario de um funcionario e acrescete um aumento de 15%. 

salario=float(input('Digite o valor do salario. '))
acrescimo=(salario/100)*15
novoSalario=salario + acrescimo 
print(f'Seu salario é de R$ {salario:.2f} e terá um aumento de R$ {acrescimo:.2f}\n onde passará a ser de R${novoSalario:.2f} ')
  