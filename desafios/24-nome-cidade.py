'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
'''
print('-' * 30)
print(f'{"Nome de Cidades":^30}')
print('-' * 30)

city_name = str(input('Digite o nome de uma cidade: '))
#print(city_name.find('Santo'))

if city_name.find('Santo') == 0:
    print(f'Sim, a cidade de {city_name}, tem "Santo" no início de seu nome.')
else:
    print(f'Não, a cidade de {city_name}, não tem "Santo" no início de seu nome.')

#print(city_name)