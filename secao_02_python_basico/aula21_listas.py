"""
Listas em Python
As listas fazem parte das coleções no Python:
As coleções permitem armazenar múltiplos itens dentro de uma única unidade,
que funciona como um container. Em Python os três tipos de coleções mais usadas
são: Listas, Tuplas e Dicionário. Vejamos nessa aula as listas.

Lista é uma coleção de valores indexada, em que cada valor é identificado por um
índice. O primeiro item na lista está no índice 0, o segundo no índice 1 e assim
por diante. EX:

índice →    0    1    2    3    4
lista  →  ['A', 'B', 'C', 'D', 'E']

Para criar uma lista com elementos deve-se usar colchetes e adicionar os itens entre
eles separados por vírgula:
"""

from turtle import clear


lista = ['A', 'B', 'C', 'D', 'E']
print(type(lista))  # type 'list'
print(len(lista))  # 5
print(lista[4])  # D
print()  # relembrando que este print é apenas para pular uma linha.
"""
No código acima, primeiro criamos uma variável do tipo lista chamada 'lista' contendo
cinco letras como seus itens. A função 'type()' traz o tipo de variável e a função 'len()'
o tamanho do objeto. Por fim, imprimimos um item da lista acessando o índice 4.

Outra característica das listas no Python é que elas são mutáveis, podendo ser alteradas
depois de terem sido criadas. Em outras palavras, podemos adicionar, remover e até mesmo
alterar os itens de uma lista.
"""
lista = ['A', 'B', 'C', 'D', 'E']
print(lista)
lista[1] = 'F'  # alteramos o item 1 da lista
print(lista)
print()
"""
Acima primeiro criamos uma lista contendo algumas letras e depois imprimimos o seu valor.
Após isso, acessamos um dos elementos dela e alteramos o valor dele para a letra "F".
"""

"""
Além de alterar elementos em listas, também é possível adicionar novos itens nela, pois já
vêm com uma coleção de métodos predefinidos que podem ser usados para manipular os objetos
que ela contém. No caso de adicionar elementos, podemos usar o método 'append()':
"""
lista = ['A', 'B', 'C', 'D', 'E']
print(lista)
lista.append('F')
print(lista)
print()
"""
Ao usar o método 'append()', adicionamos a letra 'F' no final da lista. Quando o executarmos
o código, veremos que a lista exibirá o item adicionado na última posição.

Também podemos adicionar itens na lista através do método 'insert()'. Ele usa dois parâmetros:
o primeiro vai indicar a posição na lista em que o elemento será inserido e o segundo para
informar o item que será adicionado na lista.
"""
lista = ['A', 'B', 'C', 'D', 'E']
lista.insert(1, 'G')  # aqui adicionamos a letra 'G' na posição 1 da lista
print(lista)
print()

"""
Também é possível excluir itens da lista. Para isso temos dois métodos: 'remove()' para remoção
pelo valor informado no parâmetro, e o 'pop()' para remoção pelo índice do elemento na lista;
"""
lista = ['A', 'B', 'C', 'D', 'E']
print(lista)
lista.remove('C')  # removendo o valor 'C' da lista
print(lista)
print()
"""
No código acima removemos o elemento pelo seu valor. Retiramos da lista 'lista' o item 'C'.
Vejamos agora a remoção de um item pelo seu índice:
"""
lista = ['A', 'B', 'C', 'D', 'E']
print(lista)
lista.pop(0)  # removendo o item 0 da lista.
print(lista)
print()

"""
No caso de tentarmos remover um item de uma posição inexistente, vamos obter um erro:

lista = ['A', 'B', 'C', 'D', 'E']
lista.pop(5)
IndexError: pop index out of range

No exemplo de código acima, o método 'pop()' foi usado para remover um item da lista pelo
seu índice. Mas, a posição usada como parâmetro não existe, visto que a última posição da lista
é 4, e foi usado o índice 5 para a remoção.
Outro erro vai ocorrer caso tentarmos remover um item com um valor inexistente na lista:

lista = ['A', 'B', 'C', 'D', 'E']
lista.remove('G')
ValueError: list.remove(G): G not in list

Obtemos esse erro, pois não existe na nossa lista um item de valor 'G'.
"""

"""
Outra característica das listas é que elas podem ter diferentes tipos de elemntos na sua composição.
Isso quer dizer que podemos ter strings, booleanos, inteiros, ponto flutuante ou outros tipos diferentes
de objetos na mesma lista.
"""
aluno = ['Klaudio', 47, 1.89]  # nome, idade e altura
print(type(aluno))  # type 'list'
print(aluno)
print()
"""
Essa característica heterogênea das listas é mostrada no exemplo acima, no qual criamos uma lista com
variáveis dos tipos string, inteiro e float, que representam o nome, a idade e a altura, respectivamente.
"""
valores = [9, 4, 5, 2, 8, 7, 6, 1, 12, 0]
letras = ['b', 'f', 'm', 'l', 'c', 'a', 'd', 'h']
print(valores)
print(letras)

valores.sort()
letras.sort()
print(valores)
print(letras)

# Fatiamento nas listas:
lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
print(lista[5])  # se quisermos exibir apenas o quinto item da lista
print(lista[0:8:2])  # se quisermos ir do ínicio da lista até o 8 item, pulando de 2 em 2
print(lista[-1])  # se quisermos mostrar o último item da lista
print(lista[3:])  # se quisermos ir do terceiro item até o final da lista
print(lista[-3])  # o ante-penultimo item da lista
print(lista[::2])  # exibe a lista do ínicio até o final pulando de 2 em 2 itens
print(lista[::-2])  # do final até o ínicio da lista pulando de 2 em 2 itens
print(lista[::-1])  # exibe a lista inteira do último item até o primeiro
print()
"""
Juntando listas com os métodos 'Extend()' e '+'.
Na verdade o sinal do operador de + (mais) concatena/junta as listas. E o método 'extend' vai
realmente extender uma lista com os itens de outra. Vejamos os exemplos:
"""
l1 = [0, 1, 2, 3, 4]
l2 = [5, 6, 7, 8, 9]
l3 = l1 + l2  # usando o operador '+' para juntar as listas l1 e l2

print(l1)
print(l2)
print(l3)
print()

# o método 'extend' vai funcionar de uma forma um pouco diferente; ele vai extender uma
# lista com os itens da outra lista:
l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['f', 'g', 'h', 'i', 'j']
l1.extend(l2)

print(l1)  # já imprime a lista 'l1' extendida com a lista 'l2'
print(l2)
print()

# Obs: o 'extend' também pode adicionar apenas um valor na lista, mas para isso é muito mais comum
# utilizar o método 'append'.
l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['f', 'g', 'h', 'i', 'j']
l1.extend('A')  # adicionando um 'A' a lista 'l1'

print(l1)
print(l2)
print()

"""
Usando o método 'del' para excluir itens da sua lista.
O 'del' é usado para indicar a posição do item/itens que vai ser excluído da lista.
"""
lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
print(lista)
del(lista[3:7])  # excluí os itens de 3 a 7 na lista
print(lista)
print()

l1 = ['a', 'b', 'c', 'd', 'e']
print(l1)
del(l1[1])  # excluí o item 1 da lista
print(l1)
print()

l2 = ['f', 'g', 'h', 'i', 'j']
print(l2)
del(l2[4])  # excluí o item 4 da lista
print(l2)
print()

"""
Pegando o maior valor da lista e o menor valor da lista, usando os métodos 'max()' e 'min()'
"""
valores = [23, 2, 56, 19, 21, 9, 10, 15, 7, 51, 33]
print(valores)
print(max(valores))  # vai imprimir o item que tem o maior valor da lista
print(min(valores))  # vai imprimir o item que tem o menor valor da lista
print()

"""
Criando listas com o método 'range().
"""
l1 = list(range(0, 10))  # vai criar uma lista com números de 0 até 9
print(l1)
print()

l2 = list(range(0, 100, 8))  # cria um lista de 0 a 100 pulando de 8 em 8 (multiplos de 8)
print(l2)
print()

# Já dissemos que as listas podem ter tipos diferentes de valores ao mesmo tempo; se quisermos descobrir
# que tipos estão dentro de nossa lista, podemos fazer:

l3 = ['String', True, 10, -4.5]

for item in l3:
    print(f'O tipo do item {type(item)} e seu valor é {item}.')
print()

# Joguinho de adivinhação da palavra secreta
palavra = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Suas chances acabaram! Você perdeu!')
        break
        clear(secreto_temporario)

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Opa! Você deve digitar apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in palavra:
        print(f'Muito bem! A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Que pena! A letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)

    if secreto_temporario == palavra:
        print(f'PARABÉNS! Você ganhou! A palavra secreta é {secreto_temporario}.')
        break
        clear(secreto_temporario)
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}.')

    if letra not in palavra:
        chances -= 1

    print(f'Você tem {chances} chances.')
print()
