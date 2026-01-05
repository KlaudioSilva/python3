'''
Higher Order Functions
Funções de primeira classe
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Klaudio')
    )

print(
    executa(saudacao, 'Boa Noite', 'Elma')
    )

print(
    executa(saudacao, 'Boa tarde', 'João Pedro')
    )

print(
    executa(saudacao, 'Olá', 'Arthur')
    )