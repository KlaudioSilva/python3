'''
Exercício
Exiba os índices da lista
0 → Klaudio
1 → Elma
2 → João Pedro
3 → Arthur
'''

lista = ['Klaudio', 'Elma', 'João Pedro', 'Arthur']

indice = 0
for nome in lista:
    print(indice, ' → ', nome, '-', type(lista))
    indice += 1