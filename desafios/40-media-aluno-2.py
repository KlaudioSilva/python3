'''
Crie um programa que leia as duas notas de um aluno e calcule a sua média, mostrando
uma mensagem no final, de acordo com a média atingida.
    - média abaixo de 5.0: REPROVADO
    - média entre 5.0 e 6.9: RECUPERAÇÃO
    - média 7.0 ou superior: APROVADO
'''

print('\033[92m-\033[m' * 30)
print(f'\033[91m{"CALCULE A MÉDIA DO ALUNO":^30}\033[m')
print('\033[92m-\033[m' * 30)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
resultado = ''

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')

if media < 5.0:
    print('O aluno está REPROVADO!')
elif (media >= 5.0) and (media <= 6.9):
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')