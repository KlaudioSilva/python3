# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

print('-' * 5, ' Multiplicando ', '-' * 5)
def multiplicando(*args):
    res = 1

    for nums in args:
        res *= nums
    return res

multi = multiplicando(1, 3, 5, 7, 9)
print(multi)
print(1*3*5*7*9)
print()


print('-' * 5, ' Par ou Ímpar ', '-' * 5)
def par_impar(numero):
    if numero % 2 == 0:         #se o número for 'par'
        return f'{numero} é Par'

    return f'{numero} é Ímpar'              #desnecessario o 'else' se o 'if' não executar, executa o 'return' diretamente
    
num = par_impar(7481)
print(num)
num = par_impar(538)
print(num)
num = par_impar(12)
print(num)
num = par_impar(115)
print(num)