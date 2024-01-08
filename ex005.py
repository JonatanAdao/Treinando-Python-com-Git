""" EX.:005> Faça um programa que leia um número e mostre seu sucessor e seu antecessor.    """

n=int(input('\033[1;32;45m Digite um número\033[m:'))   # lê o número digitado 
a=n-1        # antecessor do numero digitado
s=n+1        # sucessor do número digitado
print(a,n,s)
print(f'O número digitado foi \033[4;36m{n}\033[m\n e seu antecessor é \033[4;36m{a}\033[m\n e seu sucessor é \033[4;36m{s}')