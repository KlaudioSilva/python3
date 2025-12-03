#Crie um programa que leia quanto dinheiro você têm na carteira e mostre quantos doláres você pode comprar:
#use a cotação: U$1 = R$3.27

real = float(input('Quantos reais (R$) você tem na carteira: '))
compra = real / 3.27

print('Com um total de R${:.2f}, você pode comprar U${:.2f}.'.format(real, compra))
