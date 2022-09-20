"""
Desempacotamento de listas no Python

ex 1:
lista = ['Klaudio', 'Elma', 'JP', 'Tutu']
n1, n2, n3, n4 = lista

No exemplo ele esta desempacotando os valores da lisa para dentro das variáveis n1, ne2, n3, n4
"""
lista = ['Klaudio', 'Elma', 'JP', 'Tutu']
n1, n2, n3, n4 = lista
print(n2)  # exibindo o valor que foi desempacotado pra dentro da variável 'n2'
print()
"""
ex 2:
lista = ['Klaudio', 'Elma', 'JP', 'Tutu']
n1, n2, = lista

Neste exemplo vamos ter um erro: ValueError: too many values to unpack 
Esse erro nos diz que a lista tem mais valores do que as variáveis para o desempacotamento.
Podemos resolver esse erro adicionando um '*' e uma variável:
"""
lista = ['Klaudio', 'Elma', 'JP', 'Tutu']
n1, n2, * outra_lista = lista  # independente da quantidade de valores da lista, desempacotamos os valores do índice 0 e 1 pras variáveis
print(n1, n2)
print()
print(outra_lista)  # geramos uma outra lista com o restante dos valores da lista

# se tivermos uma lista muito grande e quisermos pegar apenas os dois primeiros valores e o último valor
# lista, ignorando todos os outros valores podemos fazer isso adicionando mais uma variável:
lista = ['cachorro', 'gato', 'peixe', 'galinha', 'porco', 'cavalo', 'vaca', 'ovelha', 'pato']
n1, n2, *outros, ultimo_da_lista = lista  # adicionando a variável para o último valor da lista
print(ultimo_da_lista)
print(outra_lista)
print(n1, n2)
print()

# vamos agora pegar os três últimos valores que estão na lista:
lista = ['lápis', 'borracha', 'caneta', 'caderno', 'estojo', 'clipe', 'mochila', 'apostila', 'corretivo']
*outra_lista, antepenultimo, penultimo, ultimo = lista
print(antepenultimo)
print(penultimo)
print(ultimo)
print()

# Obs: se por acaso você não está interessado ou não vai precisar dos valores restantes da lista, pode
# usar um '*_', o sinal de '_' ainda funciona como uma variável, mas indica que os valores restantes são
# desnecessários.