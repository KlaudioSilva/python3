#Escreva um programa que pergunte a quantidade de kms percorridos por um carro alugado e a quantidade de
#dias pelos quais ele foi alugado.
#Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R#0.15 por km rodado.

kms = int(input('Quantos quilômetros foram percorridos com esse carro: '))
dias = int(input('Por quantos dias ele foi alugado: '))

tot_pagar = (60 * dias) + (0.15 * kms)

print('O total a pagar pelo aluguel do carro por {} dias e com {}kms percorridos é de R${:.2f}'.format(dias, kms, tot_pagar))