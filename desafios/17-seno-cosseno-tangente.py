'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno
cosseno e a tangente desse ângulo.
'''
import math
print('-' * 2, 'Seno, Cosseno e Tangente', '-' * 2)

angulo = int(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo}º tem o Seno de {seno:.2f}')
print(f'O ângulo de {angulo}º tem o Cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo}º tem a Tangente de {tangente:.2f}')