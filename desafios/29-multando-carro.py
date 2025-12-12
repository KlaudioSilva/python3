'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80kmh mostre uma mensagem dizendo que ele
foi multado.
O custo da multa é R$7,00 por cada km acima do limite.
'''

print('-' * 30)
print(f'{"DE OLHO NO RADAR":^30}')
print('-' * 30)

kmh_atual = int(input('Qual é a velocidade atual do veículo? [kmh]: '))
kmh_acima = 0
multa = 0.0

if kmh_atual > 80:                  #se a velocidade for maior do que o limite
    kmh_acima = kmh_atual - 80      #calcular quantos kmh estão acima do limite
    multa = kmh_acima * 7           #calcular o valor da multa

    print(f'Multado! Você está {kmh_atual - 80}kmh acima do limite. Sua multa é de R${multa:.2f}')
else:
    print(f'Com a velocidade de {kmh_atual}kmh você ainda está dentro do limite de velocidade.')