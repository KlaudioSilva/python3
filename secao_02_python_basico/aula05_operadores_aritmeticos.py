"""
Operadores Aritméticos:
  + Adição
  - Subtração
  * Multiplicação
  / Divisão
  // Divisão inteira
  ** Exponenciação
  % Resto da divisão
  () Parentêses controlam a precedência da operação
"""
print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 5)
print('Multiplicação * ', 10 * 10)
print('Divisão /', 10 / 2)

# No Python o operador de multiplicação também serve como operador de repetição numa string:
print('=' * 10)  # Leve em conta que o multiplicador deve ser um inteiro

# O operador de adição também pode ser usando como concatenador entre duas strings:
print('Junte os número: ', '5' + '5')  # Ele não somou os 5, ele os juntou. Obs: não é possível concatenar int com strings

"""
A divisão inteira dá como resultado um valor inteiro
da operação executada.
"""
print(10 // 3)
print(25.3 // 4)  # se o número dividendo for um float o resultado também será um float arredondado
print()

"""
Usamos dois símbolos de astericos pra realizarmos uma exponenciação, ou
seja, elevamos um valor por outro.
"""
print(5 ** 2)
print(40 ** 3)
print()

"""
Usamos o símbolo de % para obter o resto da divisão ou módulo.
No geral só obtemos dois resultados: 0 quando a divisão é feita com 
valores pares e 1 com valores ímpares. Por isso o resto da divisão
é a melhor escolha para descobrir se um valor é par ou ímpar
"""
print(3456 % 2, ' O resto da divisão é 0, o valor é par.')
print(3455 % 2, ' O resto da divisão é 1, o valor é ímpar.')
print()

"""
Trabalhando com parenteses para alterar a precedência das operações.
"""
# Sem usar os parenteses pra mudar a precedência:
print(5 + 3 * 10)

# Usando os parenteses. Veja que o resultado mudou completamente:
print((5 + 3) * 10)
print()

"""
Veja a precedência das operações:
  1º () Os parenteses tem a maior precedência.
  2º ** Logo depois vem a exponenciação.
  3º *, /, // e % Na sequência multiplicação, divisão, divisão inteira e módulo
  4º +, - A adição e a subtração vem ao final.
"""