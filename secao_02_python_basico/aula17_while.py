"""
Estrutura de repetição WHILE.
O comando 'while' faz com que um conjunto de instruções seja executado enquanto
uma condição é atendida. Quando o resultado dessa condição passa a ser falso,
a execução do laço é interrompida.
"""
contador = 0
print('Conte de 0 a 5')
while (contador < 5):
    print(contador)
    contador = contador + 1
print('Fim')
print()
"""
Neste código, enquanto a variável contador, inicializada com 0, for menor do que 5, as
instruções das linhas 10 e 11 serão executadas.

Observe que na linha 11 incrementamos o valor da variável contador, de forma que em algum
momento seu valor igualará o número 5. Quando isso for verificado na linha 9, o laço será 
interrompido. Sem esse código, a condição de parada não será atingida, gerando o que é 
chamado de loop infinito.
"""

# pulando valores
cont = 0
print('Conte de 0 a 10 ignorando o 3 e o 7')
while (cont < 10):
    if (cont == 3) or (cont == 7):
        cont += 1
    print(cont)
    cont += 1
print('Fim')
print()

# ignorando valores ímpares
con = 0
print('Conte de 0 a 10 ignorando os número ímpares.')
while (con < 10):
    if con % 2 == 1:
        con += 1
    print(con)
    con += 1
print('Fim')
print()

# interrompa a contagem
con = 0
print('Quando a contagem chegar a 5, pare a contagem.')
while (con < 10):  # o while está comparando o con enquanto ele for menor do que 10
    con += 1
    print(con)
    if con == 5:  # mas se o con for igual a 5 interrompa (break) a contagem 
        break
print('Fim')
print()

# usando um while dentro de outro while
print('Vamos criar colunas com o while')
x = 0  # coluna

while x < 5:
    y = 0  # linha
    while y < 5:
        print(f'({x}, {y})')
        y += 1
    x += 1
print('Acabou!')
print()

"""
Até agora nossas contagens sempre mudam de linha a cada novo giro do laço, 
mas vamos agora fazer uma contagem que fica na mesma linha.
"""
cont = 0
while cont < 15:
    #  Usei o 'end=' para continuar a contagem na mesma linha e adicionar um espaço em branco entre os valores
    print(f'{cont}', end=' ')  # Aqui usei um espaço, mas poderia ser ',' ou '-' ou '→' ou qualquer outra coisa
    cont += 1
print('Terminei!')
print()

"""
Para finalizar vamos criar uma calculadora muito básica usando o laço 'while'
"""
print('~' * 20)
print(f'{"BASIC CALCULATOR":^20}')  # centralizando o titulo
print('~' * 20)

while True:
    val1 = input('Primeiro número → ')
    val2 = input('Segundo número → ')
    operador = input('Operador [+, -, *, /] → ')

    if not val1.isnumeric() or not val2.isnumeric():
        print('ERRO! Digite valores numéricos.')
        continue

    val1 = int(val1)
    val2 = int(val2)

    # operadores válidos
    while operador not in '+-*/':
        operador = input('Escolha um operador válido → ')
    print()

    # operação Adição
    if operador == '+':
        print(f'{val1} + {val2} = {val1 + val2}')
        print('-' * 20)
        print()

    # operaçao Subtração
    if operador == '-':
        print(f'{val1} - {val2} = {val1 - val2}')
        print('-' * 20)
        print()

    # operação Multiplicação
    if operador == '*':
        print(f'{val1} * {val2} = {val1 * val2}')
        print('-' * 20)
        print()

    # operação Divisão
    if operador == '/':
        if val2 == 0:
            val2 = int(input('Erro! Divisão por zero! Segundo número → '))

        print(f'{val1} / {val2} = {val1 / val2}')
        print('-' * 20)
        print()

    # sair do programa
    sair = input('Deseja encerrar? [S] ou [N]: ').strip().upper()[0]
    if sair == 'S':
        print('Saindo do programa.')
        break
print()

# Nota: Em Python, para indicar o bloco de código pertencente ao while, 
# devemos apenas indentar o código, conforme demonstrado nos exemplos acima.