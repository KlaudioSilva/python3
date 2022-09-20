"""
For / Else em Python
Como visto anteriormente, em algumas situações é comum que uma mesma instrução
(ou conjunto delas) precise ser executada várias vezes seguidas. Nesses casos,
normalmente usamos um loop (laço de repetição) que permite executar o mesmo bloco
de código enquanto uma condição for verdadeira. Em Python, os loops são codificados
com as estruturas de repetição FOR e WHILE.

O laço FOR nos permite percorrer itens de uma coleção e, para cada um deles, executar
o bloco de código declarado no loop.

Enquanto percorremos a lista de valores, a variável indicada no FOR receberá, a cada
iteração, um item da coleção. Assim, podemos executar algum processamento com esse 
elemento:
"""
nomes = ['Klaudio', 'Elma', 'João', 'Arthur']
for n in nomes:
    print(n)
print()
"""
A variável 'nomes' é uma lista inicializada com uma sequência de valores do tipo string.
A instrução FOR percorre todos esses elementos, um por vez e, em cada caso, atribui o valor
do item à variável 'n', que é impressa em seguida. Como resultado temos a impressão de todos
os nomes contidos na lista

FOR/ELSE
É possível adicionar a instrução ELSE ao final do FOR. Isso faz com que um bloco de código
seja executado ao final de uma iteração:
"""
nomes = ['Klaudio', 'Elma', 'João', 'Arthur']
for n in nomes:
    print(n)
else:
    print('Todos os nomes foram listados com sucesso!')
print()
"""
No ínicio definimos uma variável que armazenará uma lista de nomes. Após isso, a instrução FOR
percorre todos esses elementos e atribui um a um à variável 'n', que será impressa (print(n)). Após
o loop se encerrar, o bloco de código contido na instrução ELSE é acionado, imprimindo a mensagem na tela.
"""

# IF/ELSE dentro do FOR
nomes = ['Klaudio', 'Elma', 'João', 'Arthur']

for valor in nomes:
    print(valor)
    if valor.upper().startswith('J'):  # se o valor, converte p/maiúscula), começa com a letra J
        break
else:
    print('Na lista não existe uma palavra que começa com a letra "J".')
print()