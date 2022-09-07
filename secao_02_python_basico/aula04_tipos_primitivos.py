"""
Tipos de dados
str - string
int - inteiro
float - real/ponto flutuante
  Obs: os números do tipo inteiro também fazem parte dos números reais.
bool - booleano/lógico
"""

print("Dado tipo string → 'TEXTO', 'palavra', 'Klaudio', 'A', '123'")
print('Klaudio', type('Klaudio'))
print()

print('Dado tipo int → 1234, -25, 1045, 0')
print(12345, type(12345))
print()

print('Dado tipo float → 1234.51, 87.23, 0.1, -543.99')
print(0.1, type(0.1))
print()

print('Dado tipo bool → 10 == 10 (True), 10 != 10 (False)')
print(10 == 10, type(10 ==10))
print()

"""
Uma string vazia ou o número 0 também é avaliado pelo bool como False
"""
print(bool(''))
print()

# Usando type casting ─ conversão de tipo
# No exemplo a seguir convertemos a string '10' para o inteiro 10
print('10', type('10'), type(int('10')))
print()
# Obs: essa conversão só é possível porque a string era um número, se fosse um texto causaria um erro.


# Desafio simples: Tipos usando seus dados pessoais.
# String: nome
print('Klaudio', type('Klaudio'))

# Int: idade
print(47, type(47))

# Float: altura
print(1.90, type(1.90))

# Bool: maior de idade?
print('É maior de idade?', end=' → ')
print(47 >= 18, type(47 >= 18))
print()