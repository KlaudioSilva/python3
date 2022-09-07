"""
Para formatar strings em Python, primeiramente podemos usar o método 'format()', ou
como é mais comum hoje em dia usar 'fstrings'.
O método 'format()' serve basicamente para criar uma string que contém campos entre
chaves que são substituídos pelos argumentos do format.
"""
# no exemplo, o método 'format()' tem os argumentos: Klaudio e Python.
print('Olá, eu sou {}, e estou programando em {}, que é muito divertido.'.format('Klaudio', 'Python'))
print()


"""
Os campos entre as chaves estão associados aos parâmetros do método 'format()'.
Podemos usar numeração nas chaves e que essa numeração na string sempre se inicia
pelo zero para o primeiro parâmetro, um para o segundo e assim por diante (0, 1, 2...)
Podemos usar um mesmo parâmetro mais de uma vez e em fora de ordem.
Veja o exemplo:
"""
print('{0} é um {1} companheiro e um {1} programador.'.format('Klaudio', 'bom'))
print('{1} mesmo é o {0}, e {1} programador também.'.format('Silva', 'bom'))
print()


"""
Também podemos usar campos nomeados, mas esses campos devem vir depois dos
parâmetros simples no método 'format()'.
Veja o exemplo:
"""
texto = '{0} tem {idade} anos de idade'
print('CALCULANDO A IDADE DE UMA PESSOA')
print('--------------------------------')
nome = input('Qual é o nome da pessoa: ')
nasc = int(input('Em que ano a pessoa nasceu: '))
ano = int(input('Qual é o ano atual: '))
# primeiro o texto da variável, depois os parâmetros do format, o nome e um calculo simple para obter a idade.
print(texto.format(nome, idade = ano - nasc))
print()


"""
F-STRINGS:
A partir da versão 3.6 do Python, foi introduzido o conceito de f-strings. Também chamadas de 'strings 
literais formatadas'. F-strings são strings com a letra 'f' no início e chaves {} para realizar a interpolação
das expressões.
As expressões são processadas em tempo de execução e formatadas utilizando o protocolo '__format__'.
Veja os exemplos:
"""
nome = 'Klaudio'
idade = '46'
altura = 1.90
peso = 114

print(f'Oi, eu sou o {nome}, tenho {idade} anos de idade, tenho {altura} de altura e peso {peso}.')
print()

# string mult-linha
curso = 'Python do Básico ao Avançado'
aula = 'Formatando strings no Python'
dificuldade = 'Básico'

print(
    f"Curso: {curso}\n"
    f"Módulo: {aula}\n"
    f"Dificuldade: {dificuldade}"
)
print()


# DICAS EXTRAS; essas dicas servem tanto para o método 'format()', quanto para as 'F-strings':
# Alinhamento de strings
txt = 'Eu amo Python'
# alinhando a direita com espaços em branco
print('{:>20}'.format(txt))

# alinhando ao centro usando espaços em branco a esquerda e a direita
print(f'{txt:^20}')

# como formatar decimais
n1 = 1.225
n2 = 34.98765896
n3 = 0.34567
# dentro das chaves temos o parâmetro seguido de :, o ponto flutuante e a quantidade de casas decimais que serão exibidas (:.2f)
print(f'{n1:.1f}')
print(f'{n2:.3f}')
print(f'{n3:.2f}')
print()


# Resolução do desafio da aula:
nome = 'Klaudio'
idade = 46
altura = 1.9
peso = 114
ano = 2022 - idade
imc = peso / (altura ** 2)

print('-' * 40)
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {ano}.')
print()
