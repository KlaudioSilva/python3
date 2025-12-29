"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):     #a função 'soma' recebe os parâmetros X e Y
    #definição
    print(f'{x=} y={y} z={z}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)      #argumentos não nomeados
soma(y=2, x=1, z=4)  #argumentos nomeados

soma(1, y=3, z = 5)     #não é recomendável fazer dessa forma, misturar nomeado com não nomeado
print(1,2,3, sep='-')