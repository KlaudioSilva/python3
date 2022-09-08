"""
Exercício 01 - Crie um programa que peça ao usuário para digitar um
número inteiro, informe se este número é par ou ímpar. Caso o usuário
não digite um número inteiro, informe que não é um valor inteiro válido.
"""
num = input('Digite um número inteiro qualquer: ')

try:
    # tente converter num para um valor inteiro
    num = int(num)

    if num % 2 == 0:
        print(f'O número {num} é um valor PAR!')
    else:
        print(f'O número {num} é um valor ÍMPAR!')

except:
    print(f'O número {num} não é um número inteiro.')
print()
