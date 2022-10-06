"""
1 ─ Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""
def hello():
    return 'Hello World!'

def main(func):
    return func()

execute = main(hello)  # chama a função main() dando como parâmetro o 'hello world!' da função hello()
print(execute)         # printa tudo na tela
print()


"""
2 ─ Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""
def mestre(func, *args, **kwargs):
    return func(*args, **kwargs)

def ola(nome):
    return f'Olá {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(ola, 'Klaudio')
executando2 = mestre(saudacao, 'Klaudio', saudacao='Boa tarde!')
print(executando)
print(executando2)
print()