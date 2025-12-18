'''
A confederação nacional de natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    + até 9 anos: MIRIM
    + até 14 anos: INFANTIL
    + até 19 anos: JUNIOR
    + até 20 anos: SÊNIOR
    + acima: MASTER
'''

import datetime

print('\033[92m-\033[m' * 30)
print(f'\033[91m{"CLASSIFICANDO ATLETAS":^30}\033[m')
print('\033[92m-\033[m' * 30)

nasc = int(input('Ano de nascimento: '))
ano_atual = datetime.datetime.now().year

idade = ano_atual - nasc
classe = ''

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    classe = 'MIRIM'
elif (idade >= 10) and (idade <= 14):
    classe = 'INFATIL'
elif (idade >= 15) and (idade < 19):
    classe = 'JUNIOR'
elif idade == 19:
    classe = 'SÊNIOR'
else:
    classe = 'MASTER'

print(f'Classificação: {classe}')