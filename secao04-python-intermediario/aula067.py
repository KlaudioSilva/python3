"""
valores padrão para parâmetros
Ao definir uma função, os parâmetros
podem ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=} = ', x + y + z)
    else:
        print(f'{x=} + {y=} = ', x + y)

soma(1,2)
soma(3, 6)
soma(134, 234)
soma(4, 98, 0)