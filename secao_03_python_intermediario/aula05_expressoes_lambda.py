"""
Funções Lambda (Expressões Anônimas) em Python
O Python provê um tipo diferente de função denominado de função Lambda. Num primeiro momento,
funções locais (def) e expressões lambda são muito semelhantes. Em muitos casos, a escolha
entre usar expressões lambda e funções locais é uma questão de estilo e preferência pessoal.

Todas as caracteristicas de uma função lambda são muito parecidas com as funções locais, com
exceção de duas coisas: elas não possuem uma definição em código, ou seja, são declaradas
como variáveis e não possuem um def próprio; e elas são funções de uma linha, que funcionam
como se houvesse a instrução return antes do comando:
"""
def ex_soma(a, b):
    s = a + b
    return s

soma_lambda = lambda num1, num2: num1 + num2  # função soma escrita como função lambda
soma = ex_soma(10, 20)                        # chamada da função ex_soma
print('Soma = ', soma)

soma = soma_lambda(10, 20)                    # chamada da função lambda soma_lambda
print('Soma Lambda = ', soma)
print()

"""
A foma geral para criação da função lambda é:

    NomeDaFunção = lambda variavel1, variavel2,... : fórmula

As variáveis que aparecem na definição da função são os parâmetros e fórmula é a expressão
da função.
"""