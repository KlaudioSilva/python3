"""
DEF - Funções em Python - parte 1
Na programação, funções são blocos de código que realizam determinadas tarefas que normalmente
precisam ser executadas diversas vezes dentro de uma aplicação. Quando surge essa necessidade,
para que várias instruções não precisem ser repetidas, elas são agrupadas em uma função,à qual é
dado um nome que poderá ser chamada/executada em diferentes partes do programa.
"""
def ola():
    print('Olá Mundo!')

ola()
ola()
ola()
"""
Essa função, de nome 'ola', tem o objetivo de imprmir 'Olá Mundo!'. A palavra reservada 'def', explicita
a definição da função. E para executar uma função, de forma semelhante ao que ocorre em outras linguagens,
devemos simplesmente chamar seu nome.
"""
print()
"""
As funções também podem receber parâmetros. Parâmetros, basicamente, são variáveis que passamos dentro dos
parenteses nas funções.
Podemos definir funções com nenhum ou vários argumentos/parâmetros.
"""
def ola(msg):  # a função 'ola' recebe o parâmetro 'msg'
    print(msg)

ola('Bom dia!')  # ao chamar a função definimos o seu parâmetro
ola('Boa tarde!')
ola('Boa noite!')
print()

def saudacao(msg, nome):  # a função pode ter mais de um parâmetro
    print(msg, nome)

saudacao('Oi', 'Klaudio')
saudacao('Olá', 'Elma')
saudacao('Boa tarde', 'Arthur')

print()

# OBS: se o parâmetro da função não for definido na sua chamada teremos um erro:
# TypeError: funcao() missing required positional argument: 'msg'
# Uma maneira de evitar esse tipo de erro é definir parâmetros padronizados para a
# função
def hello(msg='Olá', nome='usuário'):
    print(msg, nome)

hello()  # aqui a função assume que vamos usar os valores padrão
hello('Opa', 'Klaudião')
hello('Blz', 'Arthur')
hello('Tarde', 'Chico')
print()
# Atenção! Não é possível alterar a ordem dos parâmetros. Ou seja, não dá pra inverter
# o parâmetro 'msg' pelo 'nome', apenas digitando:
# hello('Klaudio', 'Oi')
# Mas é possível fazer as inversões usando os argumentos nomeados:.

hello(nome='JP', msg='Tudo bem')
print()
