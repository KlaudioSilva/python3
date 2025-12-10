'''
Agora o professor quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia os nomes e mostre a ordem sorteada.
'''

from random import shuffle
print('-' * 40)
print(f'{"Sorteando a Ordem de Apresentação":^40}')
print('-' * 40)

nom1 = str(input('Digite o nome do primeiro aluno: '))
nom2 = str(input('Digite o nome do segundo aluno: '))
nom3 = str(input('Digite o nome do terceiro aluno: '))
nom4 = str(input('Digite o nome do quarto aluno: '))

lista = [nom1, nom2, nom3, nom4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)