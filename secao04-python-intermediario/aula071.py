"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

#lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0           #acumulador
#    for numero in args:
#        print('Total', total, numero)
#        total = total + numero
#        print('Total', total)
#    print(total)

    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

soma_7_8_9 = soma(7, 8, 9)
print(soma_7_8_9)

outra_soma = soma(1,2,3,4,5,6,7,8,9)
print(outra_soma)

#soma(1, 2, 3, 4, 5, 6)