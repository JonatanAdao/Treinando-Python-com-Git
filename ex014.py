"""
 EX.: 014 Escreva um programa que converta uma temperatura digitando em graus Celsius
 e converta para graus Fahrenheit.
"""
c = float(input('Informe a teperatura em C°.'))
f = (9/5 *c)+32
print ('Sua temperatura de {}C° foi convertida para {}F°'.format(c,f))
