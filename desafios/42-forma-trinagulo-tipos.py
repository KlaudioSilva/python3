'''
Crie um programa que leia o comprimento de três segmentos de reta e diga se
elas podem formar um triângulo e além disso, qual é o tipo de triângulo formado:
    * EQUILÁTERO: todos os lados são iguais
    * ISÓSCELES: dois lados iguais
    * ESCALENO: todos os lados são diferentes
'''

import datetime

print('\033[92m-\033[m' * 30)
print(f'\033[91m{"FORMA TRIÂNGULO? QUE TIPO?":^30}\033[m')
print('\033[92m-\033[m' * 30)

seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))

triangulo = ''
formam = ''

if (seg1 + seg2 > seg3) and (seg3 + seg2 > seg1) and (seg1 + seg3 > seg2):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')

    if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')