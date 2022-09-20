"""
SPLIT, JOIN e ENUMERATE em Python

As funções 'split()' e 'join()' servem para, respectivamente, quebrar (separar) e unir (juntor) strings.
Supondo que temos uma string com a frase: "Estou aprendendo a programar em Python", para transformar essa
string em lista de palavras separadas usaremos o 'split()':
"""

frase = 'Estou aprendendo a programar em Python'
print(frase)  # a string completa
print(frase.split())  # a lista criada com a string e as palavras divididas pelo 'split()'
print()
"""
A separação foi feita a cada espaço em branco. Mas também é possível fazer essa quebra usando quaisquer
caracteres. Vamos usar de exemploa frase: "123PI456PI789PI"
"""
frase = '123PI456PI789PI...'
print(frase)  # a string completa
print(frase.split('PI'))  # Tirando os 'PI' e criando uma lista com os elementos separados pelo 'PI'
print()

"""
Fazendo contagem dentro da lista criado com o 'split()'
"""
frase = 'O Brasil é o país do futebol, o Brasil é pentacampeão.'
lista1 = frase.split(' ')
lista2 = frase.split(',')

for valor in lista1:
    # usando a função 'count()' para contar quantas vezes cada palavra apareceu na lista criada pelo 'split()'
    print(f'A palavra "{valor}" apareceu {lista1.count(valor)} x vezes na frase.')
print()

# fazendo uma contagem para ver qual palavra aparece mais vezes na lista
frase2 = 'Olhe homem, veja o mar, veja o barco, veja o céu, veja o lindo horizonte.'
lista = frase2.split()

palavra = ''
contagem = 1

print(frase2)

for valor in lista:
    # a variável recebe a contagem da lista
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:  # se a variável for maior que contagem
        contagem = qtd_vezes
        palavra = valor
    
print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x).')
print()

"""
JOIN
Usamos o 'split()' para separar as palavras de uma string e criar uma lista, mas com a função
'join()', juntamos as palavras de uma lista para formar uma string.
Se, por exemplo, usarmos uma vírgula ou um espaço antes do 'join()', ele vai unir cada string
da lista colocando uma vírgula ou espaço, respectivamente, entre as strings:
"""
lista = ['Klaudio', 'Silva', 'programador', 'em', 'Python']
print(','.join(lista))  # unindo as palavras com vírgula
print(' '.join(lista))  # unindo as palavras com espaço
print()

# separando uma string numa lista e depois unindo a lista em uma string
string = 'O Brasil é pentacampeão.'
print(string)
lista = string.split()  # dividindo a string numa lista
print(lista)
string2 = '-'.join(lista)  # unindo a lista em uma string (fiz o join usando '-', mas poderia ser um espaço ou outro caracter)
print(string2)
print()

"""
ENUMERATE
O ENUMERATE percorre uma lista com índices, ou seja, ele pega o item da lista e enumera além da informação desejada
dessa lista.
Ele permite percorrer não apenas listas, mas qualquer estrutura iterável, ou seja, listas, dicionários, tuplas...
Pra simplificar, o método 'enumerate()' vai adicionar um contador iterável e retorna um objeto enumerado (os índices).
Por exemplo, o 'enumerate()' pega uma tupla e a retorna como um objeto enumerado:
"""
lista = ['Klaudio', 'programador', 'Python', '2022']
for i, item in enumerate(lista):  # para indice do item enumere a lista
    print(i, item)
print()

lanches = ['Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Sorvete']
for c, lanche in enumerate(lanches):
    # adicionei (+ 1) ao contador para o índice não iniciar do zero.
    print(f'Na {c + 1}ª posição encontrei o lanche {lanche}!')
print('Cheguei ao final da lista.')
print()


"""
Enumerate  →  Enumerar os elementos da lista # list
índice     →       0         1       2       3
lista      =  ['Klaudio', 'Elma', 'João', 'Arthur']

O conjunto de elementos também pode ser formado por conjuntos de elementos dentro desse primeiro.
índice     →            0                   1                    2
índ. inter →        0         1         0       1           0         1
lista      =  [['Klaudio', 'Elma'], ['João', 'Arthur'], ['Otávio', 'Bento']]
"""
lista = [['Klaudio', 'Elma', 'João', 'Arthur'], ['Paula', 'Otávio', 'Bento', 'Flávio'], ['Léia', 'Paulo', 'Pedro', 'Camila']]

print(lista[1][2])  # vai exibir da lista (do índice 1) o item 'Bento' (do índice 2)

enumerada = list(enumerate(lista))  # vai enumerar os índices das listas internas (só as listas, não os items de cada uma)
print(enumerada)

enumerada2 = list(enumerate(lista))
print(enumerada2[2][1])  # pegamos o índice 2 da tupla mãe e o índice 1 da lista filha

enumerada3 = list(enumerate(lista))
print(enumerada3[1][1][3])  # pegamos o índice 1 da tupla mãe, o índice 1 da lista filha e o item 3 da lista filha

# Relembrando: o ENUMERATE vai enumerar os elementos dentra da lista. Quando não estipulamos ao 'enumerate' que queremos
# que ele inicie a enumeração de um determinado valor, ele sempre vai iniciar do zero, o que acaba batendo com os índices:
lista = [['Klaudio', 'Elma'], ['João', 'Arthur'], ['Otávio', 'Bento']]

for v1, v2 in enumerate(lista, 15):  # aqui dizemos ao 'enumerate' para iniciar a enumeração a partir do 15
    print(v1, v2)
print()

for v1 in enumerate(lista):  # aqui escondemos os valores enumerados e exibimos apenas os valores das listas
    valor_enumerado, minha_lista = v1
    nome1, nome2 =  minha_lista
    print(nome1, nome2)
print()