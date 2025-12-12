'''
Crie um programa que pergunte a distância de uma viagem em kms.
Calcule o preço da passagem, cobrando R$0,50 para cada km em
viagens até 200km e R$0,45 para viagens mais longas.
'''

print('-' * 30)
print(f'{"CALCULANDO O CUSTO DA VIAGEM":^30}')
print('-' * 30)

distancia = int(input('Qual é a distância da viagem [Km]: '))
custo = 0.0

if distancia <= 200:
    custo = distancia * 0.50
else:
    custo = distancia * 0.45

print(f'Para uma viagem com {distancia}km de distância o custo da passagem será de R${custo:.2f}')