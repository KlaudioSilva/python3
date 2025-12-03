#Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.

salario = float(input('Qual é o seu salário atual? R$'))
aumento = salario + (salario * 15) / 100

print('Seu salário atual de R${:.2f} - com um reajuste de 15%, passará a ser de R${:.2f}'.format(salario, aumento))