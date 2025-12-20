'''
enumerate - enumera iteráveis (índices)
'''

#         0          1       2             3
#nomes =  'Klaudio', 'Elma', 'João Pedro', 'Arthur'   #assim cria-se uma tupla 
nomes = ['Klaudio', 'Elma', 'João Pedro', 'Arthur']  #usar parenteses também é um jeito de criar uma tupla 
nomes.append('Otávio')

for item in enumerate(nomes):
    indice, nome = item
    print(indice, nome)

print('-' * 50)
#fazendo a mesma coisa de um jeito mais simples
for indice, nome in enumerate(nomes):
    print(indice, nome)