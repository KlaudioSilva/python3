#Crie um programa que leia as duas notas de um aluno, calcule e mostre a média.

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('O aluno com as notas {} e {}, teve média: {}'.format(nota1, nota2, media))