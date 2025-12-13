'''
Crie um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
Para salários superiores a R$1250,00 calcule um aumento de 10%. Para salários inferiores ou 
iguais, o aumento será de 15%.
'''

print('-' * 30)
print(f'{"REAJUSTE SALARIAL":^30}')
print('-' * 30)

salario_atual = float(input('Digite o valor de seu salário atual: [R$] '))
novo_salario = 0.0
aumento = 0

if salario_atual <= 1250:           #se o salario atual for menor ou igual a 1250
    aumento = 15
    novo_salario = salario_atual + (salario_atual * 15) / 100
else:                               #se for maior do que 1250
    aumento = 10
    novo_salario = salario_atual + (salario_atual * 10) / 100

print(f'Seu salário atual de R${salario_atual:.2f}, com um aumento de {aumento}%, será agora R${novo_salario:.2f}')