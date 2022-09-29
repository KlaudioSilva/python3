"""
DEF - Funções em Python - parte 2
Na aula anterior, apenas exibimos os valores com a função print, sem retornar
explicitamene um resultado. No próximo exemplo, temos uma função que faz o cálculo
do salário e retorna o valor a ser pago conforme o número de horas trabalhadas:
"""
def calc_pagamento(qtd_horas, val_hora):
    horas = float(qtd_horas)
    taxa = float(val_hora)

    if horas <= 40:  # se a quantidade de horas for menor que 40
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd * (1.5 * taxa))
    return salario  # a função termina aqui no 'return'

horas = input('Digite a quantidade de horas trabalhadas: ')
taxa = input('Digite o valor da hora trabalhada: ')
tot_salario = calc_pagamento(horas, taxa)
print(f'O valor de seus rendimentos é R${tot_salario:.2f}' )
print()
"""
A função 'calc_pagamento()' recebe dois parâmetros, 'qtd_horas' e 'val_hora', que respresentam,
respectivamente, a quantidade de horas a serem calculadas e o valor da hora. Em seguida esses
valores são convertidos para o tipo float, já que na entrada serão recebidos como string, por
meio da instrução 'input'.
Se a quantidade de horas trabalhadas for menor ou igual a 40, calculamos o valor do salário
multiplicando as horas pelo valor de cada hora trabalhada. Se a quantidade for maior que 40,
adicionamos ao salário um valor adicional pelas horas extras. Por fim, retornamos o resultado
do cálculo (contido na variável 'salario') com a instrução 'return'.
"""

def divisao(n1, n2):
    if n2 == 0:  # se o n2 for 0 a chamada 'divide' torna-se False
        return

    return n1 / n2

divide = divisao(8, 2)

if divide:  # se divide é True
    print(divide)
else:
    print('Conta inválida.')