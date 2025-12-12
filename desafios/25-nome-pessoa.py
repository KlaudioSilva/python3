'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem
"Silva" no seu nome.
'''

print('-' * 30)
print(f'{"Tem SILVA No Nome?":^30}')
print('-' * 30)

name = str(input('Digite um nome completo: '))

if "Silva" in name:         # Silva está em name? TRUE ou FALSE
    print(f'Sim o nome {name}, tem "Silva".')
else:
    print(f'Não, o nome {name}, não tem "Silva".')