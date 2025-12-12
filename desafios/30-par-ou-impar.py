'''
Crie um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
'''

print('-' * 30)
print(f'{"É PAR OU É ÍMPAR":^30}')
print('-' * 30)

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero}, é um valor PAR!')
else:
    print(f'O número {numero} é um valor ÍMPAR!')