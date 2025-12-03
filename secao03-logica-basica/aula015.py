nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
nome_completo = (f'{nome} {sobrenome}')

idade = int(input('Quantos anos você tem: '))
altura = float(input('Qual é a sua altura: '))

print(f'Seu nome completo é {nome_completo}, você têm {idade} anos de idade e tem {altura:.2f} metro de altura.')