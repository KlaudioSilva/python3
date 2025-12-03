#Faça um programa que leia o preço de um produto e mostre o seu novo preço com um desconto de 5%.

preco_atual = float(input('Qual é o preço atual do produto, R$'))
novo_preco = preco_atual - (preco_atual * 5) / 100

print('O produto que custava R${:.2f}, com um desconto de 5% custa agora: R${:.2f}'.format(preco_atual, novo_preco))