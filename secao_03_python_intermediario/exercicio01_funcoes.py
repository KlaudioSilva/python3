"""
1 ─ Crie uma função que exibe uma saudação com os parâmetros 'saudacao' e 'nome'.
"""
def saudacao(saud, nome):
    print(saud, nome)

saudacao('Boa tarde', 'Klaudio')
print()


"""
2 ─ Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.
"""
def adicao(n1=0, n2=0, n3=0):
    val1 = int(n1)
    val2 = int(n2)
    val3 = int(n3)
    soma = val1 + val2 + val3
    return soma

val1 = input('Digite o primeiro valor da adição: ')
val2 = input('Digite o segundo valor da adição: ')
val3 = input('Digite o terceiro valor da adição: ')

total = adicao(val1, val2, val3)
print(f'O total da adição entre esses valores foi {total}.')
print()


"""
3 ─ Crie uma função que receba 2 números. O primeiro é um valor e o segundo é um
percentual (ex: 10%). Retorne (return) o valor do primeiro número somado do aumento
do percentual do mesmo.
"""
def conta(numero=0, percentual=1):
    valor1 = int(numero)
    porcento = int(percentual)

    total = valor1 + (valor1 * porcento) / 100
    return total
valor1 = input('Digite um valor inteiro qualquer: ')
porcento = input('Digite um valor para a porcentagem: ')

res = conta(valor1, porcento)
print(f'O total de {valor1} mais {porcento}% de aumento é igual a {res:.2f}.')
print()


"""
4 ─ Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne 'fizz', se o parâmetro
da função for divisível por 5, retorne 'buzz'. Se o parâmetro da função for divisível por 5
e por 3, retorne 'FizzBuzz', caso contrário, retorne o número enviado.
"""
def fizzbuzz(valor):
    num = int(valor)

    if (num % 3 == 0) and (num % 5 != 0):  # Fizz
        return 'Fizz'
    elif (num % 5 == 0) and (num % 3 != 0):  # Buzz
        return 'Buzz'
    elif (num % 3 == 0) and (num % 5 == 0):  # FizzBuzz
        return 'FizzBuzz'
    else:
        return num  # número

num = input('Digite um valor inteiro qualquer: ')
res = fizzbuzz(num)
print(f'{res}')
print()
