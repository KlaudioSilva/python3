'''
Faça um programa que leia um nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
 '''

print('-' * 30)
print(f'{"Analisando Um Nome Completo":^30}')
print('-' * 30)

name = str(input('Digite um nome completo para ser analisado: '))


lista = name.split()        #dividir e criar uma lista com a string
ultimo = len(lista) - 1     #tamanho da lista e diminuir em 1 para sair do 'range' ao printar

print(f'O primeiro nome é {lista[0]}')
print(f'O último nome é {lista[ultimo]}')