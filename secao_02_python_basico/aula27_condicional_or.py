"""
Expressão condicional com o operador OR
O operador 'or' retorna 'True' se uma das condições for verdadeira,
caso contrário retorna 'False':

x > 1 or x < 5
"""
nome = input('Digite o seu nome: ')
# imprime o nome OU a mensagem que diz que o usuário não digitou nada
print(nome or 'Você não digitou nada!')
print()

"""
O operador OR sempre precisará que uma das duas sub-expressões conectadas seja
verdadeira para que, a expressão num todo seja verdadeira:
"""
x = 1
#    (False) ou (True)
z = (x > 10) or (x < 100)
print(z)
"""
Vemos que o primeiro valor lógico é falso, enquanto o segundo é verdadeiro. Esses
valores estão ligados pelo operador OR que retorna verdadeiro caso uma das
sub-expressões o seja. Como o segundo valor lógico é verdadeiro, o valor decorrente
dessa análise lógica será verdadeiro.
"""
a = 0  # retorna Falso
b = None  # retorna Falso
c = False # retorna Falso
d = []  # retorna Falso
e = {}  # retorna Falso
f = 22  # retorna Verdadeiro
g = 'Klaudio'  # retorna Verdadeiro

variavel = a or b or c or d or e or f or g
print(variavel)  # vai imprimir a primeira variável verdadeira que ele encontrar
print()