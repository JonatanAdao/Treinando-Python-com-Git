print('Ex047: Crie um programa que mostre todos os números pares no intervalo entre 1 e 50.')

for con in range(2, 51, 2):
    print('.', end=' ') # contagen de laços 
    if con % 2 == 0:
        print(con, end=' ')
print ('fim')