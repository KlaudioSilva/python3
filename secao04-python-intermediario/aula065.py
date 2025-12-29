"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retonam None (nada).
"""

def Print(a, b, d):
    print('Variável 1')
    print('Variável 2')
    print('Variável 3')
    print('Variável 4')

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):   #caso não passe um valor, ele executa o valor atrelado
    print(f'Olá, {nome}!')

saudacao('Klaudio Silva')
saudacao('Elma')
saudacao('JP')
saudacao('Tutu')
saudacao()