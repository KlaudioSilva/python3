'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.
* Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''

print('-' * 30)
print(f'{"EMPRÉSTIMO HABITACIONAL":^30}')
print('-' * 30)

casa_valor = float(input('Valor da casa: R$'))
sal_comprador = float(input('Salário do comprador: R$'))
anos_finan = int(input('Quantos anos de financiamento? '))

#total_meses = anos_finan * 12

#valor da parcela = valor da casa dividido pelo total de meses em tantos anos...
parcela_valor = casa_valor / (anos_finan * 12)
#descobrindo quanto é 30% do salário atual do comprador
porcentagem_sal = (sal_comprador * 30) / 100

print(f'Para pagar uma casa de R${casa_valor:.2f} em {anos_finan} anos a prestação será de R${parcela_valor:.2f}.')

if parcela_valor > porcentagem_sal:
    emprestimo = 'NEGADO!'
else:
    emprestimo = 'ACEITO!'

print(f'Empréstimo {emprestimo}')