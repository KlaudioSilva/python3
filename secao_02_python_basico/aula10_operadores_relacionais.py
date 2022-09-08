"""
Operadores Relacionais:
==  →  igual
!=  →  diferente
>   →  maior
<   →  menor
>=  →  maior ou igual
<=  →  menor ou igual
"""
num1 = 5
num2 = 2

# num1 é igual a num2?
expr1 = (num1 == num2)
print(expr1)

# num1 é diferente de num2?
expr2 = (num1 != num2)
print(expr2)

# num1 é maior que num2?
expr3 = (num1 > num2)
print(expr3)

# num1 é menor que num2?
expr4 = (num1 < num2)
print(expr4)

# num1 é maior ou igual a num2?
expr5 = (num1 >= num2)
print(expr5)

# num1 é menor ou igual a num2?
expr6 = (num1 <= num2)
print(expr6)
print()

nome = str(input('Qual é o seu nome: '))
idade = int(input('Qual é a sua idade: '))

# limite para empréstimos
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
print()