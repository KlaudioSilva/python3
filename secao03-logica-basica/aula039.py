'''
Iterando string com while
'''
#       0 1 2 3 4 5 6 
#nome = 'K l a u d i o'      #Iteráveis (espaço entre as letras apenas para legibilidade)
#       7 6 5 4 3 2 1

nome = 'Klaudio'
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

pos = 0
nova_string = ''

while pos < tamanho_nome:
    letra = nome[pos]
    nova_string += (f'*{letra}')
    pos += 1

print(nova_string)