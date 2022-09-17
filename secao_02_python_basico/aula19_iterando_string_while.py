"""
Criando iterações com strings e while
Não costumamos usar muito o 'while' pra criar iterações, o comando mais usado é o 'for', mas
isso não quer dizer que não pôssamos utilizar o 'while'.
Para iterar sobre um elemento, esse elemento precisa ter índices. Ou seja tem um começo e um fim,
podemos usar um loop(laço) para passar sobre ele. De maneira genérica isso é iterar, ou seja:
Passar sobre cada elemento da string.
"""
# Veja na frase exemplo, o índice começa no 0 (o) e termina no 33 (a):
#        Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
print(tamanho_frase)
# pegando uma letra usando indices
print(frase[5])

"""
Já temos o tamanho da string usando o len na variável 'tamanhdo_frase' e com
isso podemos criar um contador dinâmico para por lado a lado o indice e o elemento
da string;
"""
while contador < tamanho_frase:
    # exibindo as letras e seu indice
    print(frase[contador], contador)
    contador += 1
print()

print('-' * 40)
print()


"""
Uma string é imutável, mas podemos criar uma nova variável para copiarmos
os elementos da outra variável e criar mais interações.
"""
frase2 = 'estudo para ser um programador'
tam_frase = len(frase2)
print(tam_frase)
cont = 0
nov_string = ''

while cont < tam_frase:
    nov_string += frase2[cont]  # isso não é soma, é concatenar
    cont += 1
    # aqui você vê a nova string sendo construída a cada laço do while
    print(nov_string)
print(nov_string)
print()

print('=' * 40)
print()


"""
Podemos usar 'if/else' para criar mais interações
vamos reaproveitar a string da primeira variável
"""
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
outra_string = ''

while contador < tamanho_frase:
    letra = frase[contador]
    # se a letra for 'r' então substitua pelo 'R'
    if letra == 'r':
        outra_string += 'R'
    else:
        outra_string += letra
    contador += 1

print(outra_string)
print()

"""
Poderíamos também pedir ao usuário que escolhesse a letra
que seria alterada usando um 'input' e uma função 'upper' 
para converter a letra pra maiuscula.

EX:
input_do_usuario = input('Escolha uma letra: ')
...
if letra == input_do_usuario:
    nov_string += input_do_usuario.upper()
...
"""