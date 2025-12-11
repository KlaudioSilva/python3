'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
* o nome com todas as letras minúsculas
* o nome com todas as letras maiúsculas
* quantas letras ao todo sem considerar espaços
* quantas letras tem o primeiro nome
'''

print('-+' * 13 + '-')
print(f'{"Brincando com Textos":^27}')
print('-+' * 13 + '-')

nome = str(input('Digite o seu nome completo: '))

print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')                   #tudo minúsculo
print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')                   #tudo maiúsculo

espacos = nome.count(' ')                                                           #contando espaços no nome
total = len(nome) - espacos                                                         #totalizando as letras sem os espaços

print(f'O total de letras do seu nome (sem considerar espaços) é: {total}')

prim = nome.find(' ')                                                               #encontrando primeiro espaço
tot_let_prim_nome = len(nome[:prim])                                                #comprimento do primeiro nome
print(f'O primeiro nome é {nome[:prim]} e o total de letras é {tot_let_prim_nome}')