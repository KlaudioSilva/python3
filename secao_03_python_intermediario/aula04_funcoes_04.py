"""
DEF - Funções em Python - parte 4
Escopo de variáveis dentro de funções - Local e Global

O escopo de uma variável indica sua visibilidade - ou seja, a partir de onde, no código,
a variável é acessível.
"""

"""
Escopo Local
Uma variável local (criada dentro de uma função) existe apenas dentro da função onde foi declarada.
As variáveis locais são inicializadas a cada nova chamada à função.
Desta forma, não é possível acessar, seu valor fora da função onde ela foi declarada. Para que possamos
interagir com variáveis locais, passamos parâmetros e retornamos valores nas funções.
"""
variavel = 'valor'  # essa é uma variável global
def func1():
    print(variavel)

def func2():
    print(variavel)

def func3():
    # apesar do mesmo nome essa 'variavel' foi criada localmente na func3, ela só pode ser editada dentro
    # da func3
    variavel = 'Outro valor'
    print(variavel)

func1()
func2()
func3()
print(variavel)  # imprime só o valor da variavel global
print()

print('-' * 60)
print()

var_global = 'Estudando a linguagem Python'
def escreve_texto():
    var_local = 'Klaudio Silva'
    print('Variável Global: ', var_global)
    print('Variável Local: ', var_local)  # acessível somente nesta função

print('\nExecutando a função "escreve_texto()": ')

escreve_texto()

print('\nTentando acessar as variáveis diretamente: ')
print('Variável Global: ', var_global)

# print('Variável Local: ', var_local)  # causa um erro: NameError: name 'var_local' is not defined
print()

# Devemos usar variáveis globais com muito cuidado, pois dificultam o entendimento do código e violam
# o encapsulamento das funções, podendo serem alteradas por qualquer função, sem que seja simples
# saber quem a alterou.

print('-' * 60)
print()

"""
Alterando variáveis globais
se tentarmos alterar o valor de uma variável global dentro de uma função, será criada na verdade uma 
nova variável local com o mesmo nome da global definida fora da função.

Muita atenção com esse comportamento, pois pode ocasionar erros graves na execução do programa.
"""
var_global = 'Aprendendo a programar na linguagem Python'
def escreve_texto():
    var_global = 'Sistema Unix'
    var_local = 'Klaudio Silva'

    print('Variável Global: ', var_global)
    print('Variável Local: ', var_local)

print('\nExecutando a função "escreve_texto()":')
escreve_texto()

print('\nTentando acessar as variáveis diretamente: ')
print('Variável Global: ', var_global)
print()


print('-' * 60)
print()


"""
Note o problema: VAR_GLOBAL foi alterada dentro da função, mas o seu valor permanece o mesmo
quando chamada novamente fora da função.
Para que uma variável global tenha seu valor alterado dentro de uma função, devemos lançar mão
da declaração global ao declará-la (e antes de inicializá-la.):
"""
var_global = 'Aprendendo a programar na linguagem Python'
def escreve_texto():
    global var_global  # declarando a variável global e alterando o seu valor
    var_global = 'Sistema Unix'
    var_local = 'Klaudio Silva'

    print('Variável Global: ', var_global)
    print('Variável Local: ', var_local)

print('\nExecutando a função "escreve_texto()":')
escreve_texto()

print('\nTentando acessar as variáveis diretamente: ')
print('Variável Global: ', var_global)
print()
# OBS: Não devemos usar a palavra global na mesma linha onde é atribuído o novo valor à
# variável global dentro da função.