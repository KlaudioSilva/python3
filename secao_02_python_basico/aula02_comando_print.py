# o camando 'print' é usado principalmente como saída padrão para os dados ou informações do programa

print(12345)  # ao exibir tipos numéricos não precisamos de aspas

print('12345')  # mas se os número estiverem entre aspas, o tipo de dado deixa de ser numérico para ser do tipo string

print('José', 'Arthur', 'Elma', 'João Pedro')  # o tipo string são textos, palavras ou apenas caracteres.

"""
Uma dica legal! Se usarmos o argumento 'sep=' podemos inserir algum tipo de separador entre as strings,
no exemplo abaixo eu usei um sinal de hífen (-), mas pode ser qualquer outra coisa: uma vírgula, um ponto,
um espaço, uma seta, etc...
"""
print('Klaudio', 'Elma', sep='-')
print('Klaudio', 'e', 'Elma', sep='→')

"""
Por padrão ao final de cada print temos uma quebra de linha, mas se usamos o argumento 'end=' no final do
print podemos eliminar essa quebra de linha e, assim como no 'sep=', é possível usar alguns símbolos, caracteres,
ou espaço vazio:
"""
print('Klaudio', 'Elma', sep='-', end='')  # Eliminando a quebra de linha, mas deixando tudo junto
print('Arthur', 'João Pedro')
print()  # esse print vazio serve como uma quebra de linha.

print('Klaudio', 'e', 'Elma', sep='→', end='-')  # Usando um hífen
print('JP', 'e', 'Arthurzinho', sep='-')
print()

print('Klaudio', 'Elma', 'JP', 'e', 'Arthurzinho', sep=' ', end=' ')  # Usando espaços entre as strings e eliminando a quebra de linha
print('Otávio', 'e', 'Pedro', sep=' ')
print()

# ATENÇÃO! O Python diferencia letras maiúsculas de minúsculas.
# Portanto, não existe por exemplo 'Print', o correto é 'print'

"""
Como um pequeno exercício, vamos criar um cpf com as devidas
máscaras de ponto e hífen. ex: 325.457.235-44
"""

print('824', '176', '070', sep='.', end='-')
print('18')
print()
