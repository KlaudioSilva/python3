"""
DEF - Funções em Python - parte 3
*args  **kwargs
*Args e **Kwargs permitem que você passe um número não especificado de argumentos para uma função.
Dessa forma, ao escrever uma função, você não precisa definir quantos argumentos serão passados para
sua função.
"""
"""
Argumenos não nomeados → *args:
O *args é usado para receber uma lista de argumentos de comprimento variável sem a palavra-chave
(keyword) na função:
"""
def funcao_com_argumentos_variaveis(arg, *args):
    print('Primeiro argumento: ', arg)

    for argumento in args:
        print('Argumento de *args', argumento)

funcao_com_argumentos_variaveis('primeiro_arg', 'arg2', 'arg3', 'arg4')
print()

# Argumentos não nomeados (*args) vem sempre primeiro que os argumentos nomeados (**kwargs):
# def funcao_com_argumentos_variaveis(arg='arg', 'arg2', 'arg3', 'arg4'):
# Causaria o seguinte erro:
# SyntaxError: positional argument follows keyword argument

print('-' * 60)
print()

"""
Vejamos um exemplo de função que soma os argumentos passados, independente do número de
argumentos que seja passado:
"""
def adicao(*args):
    resultado = 0

    for argumento in args:
        resultado += argumento
    return resultado

print(adicao(1, 2))
print(adicao(1, 2, 4, 6))
print(adicao(1, 2, 4, 6, 8, 10))
print(adicao(3, 5, 7, 9, 11, 13, 15))
print()


print('-' * 60)
print()


"""
Argumentos nomeados **kwargs
O **kwargs possibilita verificarmos os parâmetros nomeados da função, isto é, aqueles parâmetros que são 
passados com um nome!
Eles estarão disponíveis como um dicionário ({'chave': 'valor'}) dentro da função:
"""
def concatena(**kwargs):
    print(f'Valores recebidos: {kwargs}')  # imprime um dicionário com os nomes dos argumentos e seus valores
    resultado = ''

    for valor in kwargs.values():
        resultado += f'{valor} '
    return resultado

print(concatena (a='Aprendendo', b='programar', c='Python'))
print()
print(concatena(a='Paixão', b='por', c='programar', d='na', e='linguagem', f='Python'))
print()


print('-' * 60)
print()


# para melhor entender vamos juntar tudo e printar o que vem em cada um dos tipos de argumentos:
def funcao(arg_1, arg_2, *args, arg_kw, **kwargs):
    print(f'Parâmetro 1: {arg_1}')
    print(f'Parâmetro 2: {arg_2}')
    print(f'*args: {args}')
    print(f'Argumento nomeado: {arg_kw}')
    print(f'**kwargs: {kwargs}')

# chamada da função
funcao(
    1,            # parâmetro 1
    'a',          # parâmetro 2
    'arg1',       # *args
    'arg2',       # *args
    2,            # *args
    arg_kw='KW',  # arg_kw
    banana='B',   # **kwargs
    bananas='A'   # **kwargs
)
print()

print('-' * 60)
print()

# desempacotando duas listas dentro de uma tupla:
def func(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2)  # ao desempacotar as duas listas serão mescladas na tupla
print()

# OBS: Escrevar *args e **kwargs é apenas convenção: *args vem do inglês 'arguments'
# (argumentos) e **kwargs vem do inglês 'keyword arguments' (argumentos nomeados).
# Mas poderíamos usar qualquer outra palavra, por exemplo: *banana, **bananas.