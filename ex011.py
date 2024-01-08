"""    
EX.:011> Faça um program que leia a altura e largura de uma parede em metros,
calcule sua area e a quantidade de de tinta para pinta-la. Sabendo que cada litro de tinta pinta uma area de 2m².
"""
    #1> ler altura e largura
altura=float(input('Informe altura.'))
largura=float(input('Informe largura.'))
  #2> calcule area
calculoArea=altura*largura
print(f'Aa reia a ser pintada é de {calculoArea:.2f}m²')
litro=calculoArea/2
print(f'Para esta area de {calculoArea:.2f} vc gastara {litro} de tinta.')