'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira:
Ex:. Digitado: 6.127
     Inteiro:  6
'''
import math     #importando a biblioteca Matemática
print('-' * 5, 'Real para Inteiro', '-' * 5)

real = input('Digite um número real qualquer: ')
n_real = float(real)            #garantindo que o digitado é um número real

inteiro = math.trunc(n_real)    #convertendo para valor inteiro

print(n_real)