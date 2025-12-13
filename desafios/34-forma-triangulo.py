'''
Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo.
'''

print('-' * 30)
print(f'{"PODE FORMAR UM TRIÂNGULO":^30}')
print('-' * 30)

reta1 = int(input('Digite o comprimento da primeira reta: '))
reta2 = int(input('Digite o comprimento da segunda reta: '))
reta3 = int(input('Digite o comprimento da terceira reta: '))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print(f'As retas com comprimentos de A:{reta1}, B:{reta2} e C:{reta3}, podem formar um triângulo.')
else:
    print(f'As retas com comprimentos A:{reta1}, B:{reta2} e C:{reta3}, não podem formar um triângulo.')