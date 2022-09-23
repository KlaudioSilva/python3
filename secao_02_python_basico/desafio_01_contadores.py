# Desafio 01
# Criando dois contadores com estruturas de repetição:
# Tudo dentro do mesmo laço, um contador contando de forma progressiva
# e o outro contando de forma regressiva.
c1 = 0
c2 = 10

while c1 <= 10:  # 1º laço → enquanto o contador 1 for menor ou igual a 10...
    while c2 >= 0:  # 2º laço → enquanto contador 2 for maior ou igual a 0...
        print(c1, c2)  # exibindo
        # incrementando os contadores
        c2 -= 1
        c1 += 1
print('Fim das contagens!')
print()

"""
Usando um laço FOR:

for p, r in enumerate(range(10, 1, -1))
    print(p, r)
"""