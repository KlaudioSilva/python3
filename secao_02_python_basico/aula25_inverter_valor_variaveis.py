"""
Trocando/Invertendo valores entre varáveis no Python.
Para trocar os valores entre variáveis em outras linguagens seria necessário criar uma terceira
variável para fazermos a troca:

x = 'Klaudio'
y = 'Elma'

z = x
x = y
y = z

Em Python a troca de valores entre variáveis é muito mais simplificada. Não será necessário uma
terceira variável, basta:
x, y = y, x
"""

a = 'Shaka'
b = 'Arioria'
print(f'Antes da inversão:\n'
      f'O cavaleiro de ouro "A" é {a} e o cavaleiro de ouro "B" é {b}')
a, b = b, a
print()

print(f'Depois da inversão:\n'
      f'O cavaleiro de ouro "A" é {a} e o cavaleiro de ouro "B" é {b}')
print('-' * 60, '\n')  # usei o '\n' pra pular uma linha

x = 'Klaudio'
y = 'Elma'
z = 'JP'
print(f'Antes da inversão:\n'
      f'X = {x} e Y = {y} e Z = {z}')
print()

x, y, z = z, x, y
print(f'E depois da inversão:')
print(f'X = {x} e Y = {y} e Z = {z}')
print()