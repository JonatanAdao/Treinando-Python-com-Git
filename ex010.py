#     EX.:010> Faça um programa leia quanto dinhero a pessoa tem na carteira e converta em dolares.

din=float(input('Quanto reais vc tem na carteira? '))
print(f'Você tem hoje R$ {din:.2f} na carteira.')
conv=float(input('Informe o valor do dolar(US$) hoje? '))
print(f'O Dolar hoje esta no valor de US$ {conv:.2f}')
convXdin=din/conv
print(f'Convertendo o valor de {din:.2f} para o Dolar vc tera US$ {convXdin:.2f} de Dolar. ')
