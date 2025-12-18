'''
Crie um programa que leia dois números inteiros e compare-os, mostrando na tela
uma mensagem:
    - o primeiro valor é Maior:
    - o segundo valor é Maior
    - Não existe valor maior, os dois são iguais.
'''

print('-' * 30)
print(f'{"COMPARE DOIS VALORES":^30}')
print('-' * 30)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num2 > num1:
    print('O SEGUNDO valor é maior.')
else:
    print('Não existe valor maior, os dois são IGUAIS.')