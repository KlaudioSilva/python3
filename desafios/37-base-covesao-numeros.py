'''
Crie um programa que leia um número inteiro qualquer e peça ao usuário para
escolher qual será a base de conversão:
    - 1 para Binário
    - 2 para Octal
    - 3 para Hexadecimal
'''

print('-' * 30)
print(f'{"BASE DE CONVERSÃO":^30}')
print('-' * 30)

numero = int(input('Digie um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    converte = bin(numero)
    base = 'BINÁRIO'
elif opcao == 2:
    converte = oct(numero)
    base = 'OCTAL'
elif opcao == 3:
    converte = hex(numero)
    base = 'HEXADECIMAL'

print(f'{numero} convertido para {base} é igual a {converte[2:]}')  #usando fatiamento pra remover os prefixos