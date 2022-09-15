"""
Manipulando Strings.
* String indices
* Fatiamento de strings [início: fim: passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Indices da string
positivo  →  [012345]
texto     =  'Python'
negativo  → -[543210]
"""

texto = 'Curso de Python'

# [3] pega a letra que está no indice 3
nova_str = texto[3]
print(nova_str)

# [:3] exibe as 3 primeiras letras do indice (lembre que indice no Python começa do 0)
nova_str = texto[:3]
print(nova_str)

# pega a última letra da string
nova_str = texto[-1]
print(nova_str)

nova_str = texto[0:14:2]
print(nova_str)

# len → o comprimento da string
print(len(texto))