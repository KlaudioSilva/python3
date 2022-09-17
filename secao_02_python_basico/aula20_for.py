"""
For in em Python
O laço 'for' nos permite percorrer os itens de uma coleção e, para cada um deles,
executar o bloco de código declarado no loop:
    for variavel in lista
        comandos

Enquanto percorremos a lista de valores, a variável indicada no for receberá, a cada
iteração, um item da coleção. Assim, podemos executar algum processamento com esse 
elemento:
"""
texto = 'Python'
# para cada letra na variável 'texto'
for letra in texto:
    print(letra)
print()


nomes = ['Pedro', 'João', 'Letícia', 'Arthur', 'Otávio', 'Paula', 'Elma', 'Bento', 'Klaudio']
for n in nomes:
    print(n)
print()
"""
A variável 'nomes' é uma lista inicializada com uma sequência de valores do tipo string. A
instrução 'for' percorre todos esses elementos, um por vez e, em cada casa, atribui o valor
do item à variável 'n', que é impressa em seguida. O resultado, então, é a exibição de todos
os nomes contidos na lista.
"""

"""
Iterando strings com um laço 'for'
Função range(start=0, stop, step=1)
A função built-in 'range' não depende do laço for e nem a função 'range' depende do laço 'for',
porém podemos usar essa função junto ao 'for' para criarmos range de números:
"""
for num in range(10):
    print(num)
print()
"""
A função 'range' recebe três parâmetros: um argumento 'start', um 'stop' e um 'step'. Sendo que,
o argumento 'start' é o argumento de ínicio, ou seja, onde eu quero que ela inicie. O argumento
'stop' é justamente até onde queremos ir ou parar. E por fim, o argumento 'step', são os passos,
ou de quantos em quantos passos queremos pular.
Por padrão o 'start' sempre inicia no zero (0) e o 'step' é de um (1) passo de cada vez.
Veja o exemplo de uma contagem que inica no 0 vai até 10 pulando de 1 em 1:
"""
for n in range(0, 10, 1):
    print(n)
print()
"""
Dica: por estarmos usando os valores padrão para o 'start' e o 'step', eles podem ser omitidos
sem qualquer problema:
"""
for n in range(10):
    print(n)
print()

"""
Se usarmos um 'start' maior que o 'step', não aconteceria nada, afinal a cada volta do laço
ele acrescenta mais um na contagem e o start já é maior do que o fim da contagem:
"""
for n in range(20, 10):
    print(n)
print()
"""
Nesses casos fazemos uma contagem negativa, ou contagem regressiva. Para isso transformamos o
'step' num valor negativo:
"""
for n in range(20, 10, -1):  # aqui usei o 1 mas pode ser o valor que eu quiser
    print(n)
print()

# Usando o exemplo de tranformação de letra de minúscula para maiúscula na iteração usando o 'for'
texto = 'Python'
nov_string = ''

for letra in texto:
    if letra == 't':
        nov_string = nov_string + letra.upper()
    elif letra == 'h':
        nov_string += letra.upper()
    else:
        nov_string += letra
print(nov_string)
print()

"""
Assim como no 'while', no 'for' podemos usar dois comandos que afetam a execução do nosso laço:
→ continue ─ que pula para o próximo laço
→ break ─ que termina a execução do laço
Vejamos os exemplos:
"""
texto = 'Python'
nov_string = ''

for letra in texto:
    if letra == 't':
        continue  # ele vai pular o 't' na nova string, mas continua os outros laços
        nov_string = nov_string + letra.upper()
    elif letra == 'h':
        nov_string += letra.upper()
    else:
        nov_string += letra
print(nov_string)
print()

print('-' * 40)

texto = 'Python'
nov_string = ''

for letra in texto:
    if letra == 't':
        nov_string = nov_string + letra.upper()
    elif letra == 'h':
        nov_string += letra.upper()
        break  # ele vai terminar de vez a execução dos laços
    else:
        nov_string += letra
print(nov_string)
print()