"""
Operadores Lógicos.
Os operadores lógicos nos possiblitam construir um tipo de teste muito
útil e muito utilizado em qualquer programa Python: os testes lógicos.

Python nos disponibiliza três tipos de operadores lógicos: o AND, o OR e o NOT.

AND  →  retorna True se as duas condições forem verdadeiras
OR   →  retorna True sempre que ao menos uma das condições for verdadeira
NOT  →  retorna False se a condição for verdadeiro e retorna True se a condição for falsa
        o operador NOT inverte a condição.

"""
num1 = 7
num2 = 4

# and
if num1 > 3 and num2 < 8:
    print('As duas condições são verdadeiras.')

# or
if num1 > 4 or num2 <= 8:
    print('Uma ou duas condições são verdadeiras.')

# not
if not (num1 > 30 and num2 > 8):
    print('Inverte o resultado da condição entre os parênteses.')
# print()

"""
Podemos usar também, os operadores IN e NOT IN.
"""
nome = 'Klaudio'

if 'u' in nome:
    print(f'Existe a letra U em {nome}')
else:
    print(f'Não existe a letra U em {nome}')
print()  # usei para adicionar uma linha vazia

if 'J' not in nome:
    print(f'A letra J não existe em {nome}')
else:
    print(f'Existe J em {nome}')
print()

# veja o exemplo de um sistema de login super simples
usuario = str(input('Nome do usuário: '))
senha = int(input('Senha do usuário: '))

usuario_bd = 'jose'
senha_bd = 123456

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou Senha inválidos!')
print()
