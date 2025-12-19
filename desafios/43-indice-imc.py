'''
Crie um programa que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status
de acordo com a tabela abaixo:
    -> abaixo de 18.5: Abaixo do peso
    -> entre 18.5 e 25: peso ideal
    -> 25 até 30: sobrepeso
    -> 30 até 40: obesidade
    -> acima de 40: obesidade mórbida
'''
import math
print('\033[92m-\033[m' * 30)
print(f'\033[91m{"ÍNDICE DE MASSA CORPORAL":^30}\033[m')
print('\033[92m-\033[m' * 30)

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / math.pow(altura, 2)

print(f'O IMC dessa pessoa é de {imc:.2f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif (imc >= 18.5) and (imc < 25):
    print('Parabéns, você está na faixa de PESO NORMAL.')
elif (imc >= 25) and (imc < 30):
    print('Cuide-se, você está com SOBREPESO.')
elif (imc >= 30) and (imc < 35):
    print('Você está em OBESIDADE!')
elif imc >= 35:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')