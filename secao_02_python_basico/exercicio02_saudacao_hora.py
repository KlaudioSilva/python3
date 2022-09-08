"""
Exercício 02 - Faça um programa que pergunte a hora ao usuário e, baseando-se no
horário descrito, exiba a saudação apropriada. Ex:
00-11 Bom dia, 12-17 Boa tarde, 18-23 Boa noite.
"""
hora = input('Digite a hora atual: ')

# tente converter a hora digitada para um valor inteiro
try:
    hora = int(hora)
except:
    print('Hora inválida!')

if (hora < 0) or (hora > 23):
    print('Hora inválida!')

elif hora < 12:
    print('Bom dia!')

elif hora < 18:
    print('Boa tarde!')

else:
    print('Boa noite')
print() 
