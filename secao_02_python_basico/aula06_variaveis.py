"""
Variáveis: é a representação simbólica dos elementos de certo conjunto. Cada variável
corresponde a uma posição na memória, cujo o conteúdo pode ser alterado durante a
execução do programa. Embora uma variável possa assumir diferentes valores, ela só
pode armazenar um valor a cada instante.

Devemos inicar uma variável com uma letra, ela pode conter números, separar usando '_',
e letras minúsculas.
"""

# string
nome = 'Klaudio Silva'
# int
idade = 46
# float
altura = 1.90
# bool
e_maior = idade > 18
peso = 114.5
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print()