'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo os nomes e mostrando o nome escolhido.
'''

print('-' * 30)
print(f'{"Sorteando um nome":^30}')     #centralizando o texto da string
print('-' * 30)

import random
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

lista = [nome1, nome2, nome3, nome4]

escolhido = random.choice(lista)

print(f'O nome do aluno escolhido para apagar o quadro é {escolhido}.')