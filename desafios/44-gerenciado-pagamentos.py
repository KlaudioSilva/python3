'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e a condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

#print('\033[92m-\033[m' * 30)
#print(f'\033[91m{"TEXTO AQUI":^30}\033[m')
#print('\033[92m-\033[m' * 30)
print('\n')

print('\033[96m=\033[m' * 12, f'\033[94m{"LOJAS PYTHON"}\033[m', '\033[96m=\033[m' * 12)

preco = float(input('Preço das compras: R$'))

print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')

opcao = int(input('Qual é a sua opção? '))

if opcao == 1:
    desconto = (preco * 10) / 100
    print(f'Sua compra de R${preco:.2f} vai custar R${(preco - desconto):.2f} no final.')
elif opcao == 2:
    desconto = (preco * 5) / 100
    print(f'Sua compra de R${preco:.2f} vai custar R${(preco - desconto):.2f} no final.')
elif opcao == 3:
    print(f'Sua compra de R${preco:.2f} será parcelada em 2x de R${(preco / 2):.2f} SEM JUROS.')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))     #em quantas parcelas vai pagar
    preco_juros = preco + (preco * 20) / 100        #novo preco com os juros de 20%
    
    print(f'Sua compra será parcelada em {parcelas}x de R${(preco_juros/ parcelas):.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${preco_juros:.2f} no final.')
else:
    print('\033[36m-\033[m' * 52)
    print('\033[91mOPÇÃO INVÁLIDA!\033[m \033[92mEscolha uma das opções de pagamento.\033[m')
    print('\033[36m-\033[m' * 52)