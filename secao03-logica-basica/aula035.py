"""
Contadores com While
"""

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Fim da contagem!')
print('-' * 20)

#---------------------------------------------------------

contador2 = 0

while contador2 < 30:
    contador2 += 1

    if contador2 % 2 == 0:
        print(contador2)

print('Fim da contagem pulando de 2 em 2')
print('-' * 20)

#----------------------------------------------------------

regressiva = 10

while regressiva >= 1:
    regressiva -= 1
    print(regressiva)

print('Fim da contagem regressiva!')