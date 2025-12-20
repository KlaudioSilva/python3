"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutiláveis - índices e fatiamento
Métodos úteis:
    append - adiciona um item ao final da lista
    insert - Adiciona um item no índice escolhido
    pop    - Remove do final da lista ou do índice escolhido
    del    - apaga um índice
    clear  - limpa a lista
    extend - estende a lista
    +      - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#         01234
#        -54321
string = 'ABCDE'    #5 caracteres
#print(bool([]))    #falsy
#print(lista, type(lista))

#        0    1      2               3    4
#       -5    4      3               2    1
lista = [123, True, 'Klaudio Silva', 1.2, []]       #suporta qualquer tipo de valor(inclusive outra lista)
print(lista)

#podemos imprimir o item escolhido da lista, usar um método nesse item, descobrir o seu tipo...
print(lista[2].upper(), type(lista[2]))

print('\033[91m-\033[m' * 40)

#como já foi dito a lista é mutável, então podemos mudar um ou mais itens dela:
lista[-3] = 'João Pedro'        #usando indice negativo apenas por didática

print(lista[2].upper(), type(lista[2]))
print(lista)                    #a lista com a alteração do item 2(-3)


print('\033[91m-\033[m' * 40)

#         0   1   2   3   4   5   6   ...
lista2 = [10, 20, 30, 40]
lista2[2] = 300
print(lista2)
del lista2[2]
print(lista2)
print(lista2[2])
lista2.append(50)
lista2.pop()
lista2.append(60)
lista2.append(70)
ultimo_item = lista2.pop()
print(lista2, 'Removido último item: ', ultimo_item)


print('\033[91m-\033[m' * 40)

#         0   1   2   3
lista3 = [10, 20, 30, 40]
lista3.append('Klaudio')
nome = lista3.pop()
lista3.append(1234)
del lista3[-1]
#lista.clear()
lista3.insert(100, 5)
print(lista3[4])
print(lista3)


print('\033[91m-\033[m' * 40)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b         #a lista c vai receber as listas A e B concatenadas
print(lista_c)

lista_a.extend(lista_b)             #a lista A se extende para receber a lista B
print(lista_a)



print('\033[91m-\033[m' * 40)
'''
Cuidados com listas mutáveis
= - copiado do valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''
list_a = ['Klaudio', 'Elma', 1, True, 1.2]
list_b = list_a         #aqui a lista B está apenas apontando para a lista A
list_b = list_a.copy()  #aqui a lista B está recebendo uma cópia da lista A

list_a[0] = 'Outro nome'
print(list_a)
print(list_b)