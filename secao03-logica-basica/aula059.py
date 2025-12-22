"""
Desempacotamento em chamadas
de métodos e funções
"""
print()

string = 'ABCD'
lista = ['Klaudio', 'Elma', 1, 2, 3, 'JP', 'Tutu']
tupla = 'Python', 'é', 'legal'

p, b, *_, ap, u = lista
print(p, u, ap)

print('\033[32m-\033[m' * 50)

print('Klaudio', 'Elma', 'João Pedro', 'Arthur')
print(*lista)       #usar o asterisco '*' vai exibir cada item da lista
print(*string)       
print(*tupla)

print('\033[32m-\033[m' * 50)

print(*lista, sep='\n')     #exibe cada item da lista em uma linha separadamente