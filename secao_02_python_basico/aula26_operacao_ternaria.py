"""
Operações ternárias em Python

<expressao1> if <condicao> else <expressao2>
Primeiro, a condição é avaliada, se a condição for verdadeira, 'expressao1' é
avaliada e seu valor é retornado; caso contrário, 'expressao2' é avaliada e 
seu valor retornado:
"""
logged_user = True
# exiba msg se usuário logado, se usuário não estiver logado exiba outra msg
msg = 'Usuário logado.' if logged_user else 'Usuário offline.'
print(msg)
print()

idade = input('Digite a sua idade: ')

if not idade.isnumeric():
    print('Erro! Digite um valor numérico.')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Acesso Liberado!' if maior else 'Acesso Negado!'  # operação ternária
print(msg)
print()
