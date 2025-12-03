#formatando Strings usando fstrings
nome = 'Klaudio Silva'
altura = 1.9
peso = 119
imc = peso / (altura * altura)           #IMC = peso / (altura x altura)

print(f'{nome} tem {altura:.2f} de altura,')    #usando 'fstring' para formatar o print
print(f'pesa {peso} quilos e seu IMC é')
print(f'{imc:.2f}')