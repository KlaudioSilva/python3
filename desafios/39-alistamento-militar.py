'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com 
a sua idade:
    - se ele ainda vai se alistar ao serviço militar
    - se já é hora de se alistar
    - se já passou do tempo do alistamento
O programa também deve mostar o tempo que falta ou que passou do prazo.
'''

#primeiro passo usar a biblioteca datetime para pegar o ano atual do sistema
import datetime

print('\033[92m-\033[m' * 30)
print(f'\033[91m{"ALISTAMENTO MILITAR":^30}\033[m')
print('\033[92m-\033[m' * 30)

nasc = int(input('Ano de nascimento: '))

#descobrindo o ano atual
ano_atual = datetime.datetime.now().year

idade = ano_atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    falta = 18 - idade
    print(f'Ainda faltam {falta} para o alistamento')
    print(f'Seu alistamento será em {ano_atual + falta}')
elif idade > 18:
    passou = idade - 18
    print(f'Você já deveria ter se alistado há {passou} anos.')
    print(f'Seu alistamento foi em {ano_atual - passou}')