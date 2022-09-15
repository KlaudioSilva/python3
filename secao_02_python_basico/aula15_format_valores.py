"""
Formatando valores com modificadores.

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:.(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - alinhamento a Esquerda
< - alinhamento a direita
^ - alinhamento ao centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
# para reduzir o número de casas decimais usamos ':.2f', que arredonda para apenas duas casas decimais
# mas poderia ser com uma (:.1f), três (:.3f) ou outro valor que eu quisesse.
print(f'{divisao:.2f}')
print()

"""
Podemos formatar a saída de uma váriavel com alinhamentos e adição de algumas casas.
Por exemplo: uma variável com um valor 1, podemos mostrar esse valor alinhado a direita, a esquerda
ou ao centro adicionando algumas casas à variável. Obs não é alterado o valor da variável, apenas formatamos
sua saída com as casas que servem apenas pra preencher a saída.
"""
n1 = 1
# alinhamos a esquerda e preenchemos com o '0' as dez casas 
print(f'{n1:0>10}')

# alinhamos a direita...
print(f'{n1:0<10}')

# alinhamos ao centro...
print(f'{n1:0^10}')

# conbinando os modificadores
n2 = 1221
print(f'{n2:0>10.2f}')

print()

# fazendo alinhamentos com strings
nome = 'Klaudio'
print(f'{nome:#<20}')
print(f'{nome:@^20}')
print(f'{nome:&>20}')
# no exemplo abaixo centralizamos a variável entre 20 espaços vazios
print(f'{nome:^20}')

print()

# formantando usando funções built-in
nome = nome.ljust(15, '+')
print(nome)

print(nome.lower())

print(nome.upper())