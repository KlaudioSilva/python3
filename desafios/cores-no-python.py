'''
Para exibir cores no terminal usamos código ANSI:
Sempre inicia usando: \033[ e termina usando a letra "m"
Ex:.  \033[0;33;44m
No exemplo acima o texto/palavra não tem nenhum estilo (negrito, underline ou
negativo), mas a fonte terá a cor amarela e o fundo terá a cor azul.
'''

"""
    STYLE                TEXT               BACKGROUND
    0 → None             30 → White         40 → White
    1 → Bold             30 → Red           40 → Red
    4 → Underline        30 → Green         40 → Green
    7 → Negative         30 → Yellow        40 → Yellow
                         30 → Blue          40 → Blue
                         30 → Purple        40 → Purple
                         30 →               40 → 
                         30 → Gray          40 → Gray
"""

print('-+' * 5 + '-')
print(f'{"PRÁTICA":^11}')
print('-+' * 5 + '-')

print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')

print('\033[31m-\033[m' * 30)

A = 3
B = 5
print(f'Os valores são \033[32m{A}\033[m e \033[31m{B}\033[m!!!')

print('\033[31m-\033[m' * 30)

nome = 'Klaudio Silva'
print(f'Olá! Muito prazer em te conhecer \033[4;33m{nome}\033[m.')

print('\033[31m-\033[m' * 30)

nome2 = str(input('Digite um nome: '))
#criando uma lista de cores:
cores = {
    'Limpa':'\033[m',
    'Azul':'\033[34m',
    'Amarelo':'\033[33m',
    'PretoBranco':'\033[7;30m'
}

#funcionou bem com 'format'
print('Olá! Muito prazer em te conhecer {}{}{}'.format(cores['Azul'], nome2, cores['Limpa']))
#não funcionou com f'strings
#print(f'Olá! Muito prazer em te conhecer {cores["Azul"], nome2, cores["Limpa"]}')