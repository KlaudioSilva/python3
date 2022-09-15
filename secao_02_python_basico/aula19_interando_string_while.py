"""
Criando iterações com strings e while
"""
#        Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
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
    nov_string += frase2[cont]
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