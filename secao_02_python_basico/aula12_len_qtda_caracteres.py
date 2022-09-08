"""
Método Len().
Len() é uma função integrada ao Python que é utilizada para obter o número de itens
em um determinado objeto, string, array, listas, entre outros (exceto para valores numéricos).
Quando aplicamos a função Len() em uma string por exemplo, ela retorna a quantidade de caracteres
que possui, ou seja, o comprimento da string.
"""
nome = str(input('Digite o seu nome: '))
qtd_caracter = len(nome)

print(nome, qtd_caracter)

if qtd_caracter < 6:
    print('Você tem um nome com menos de 6 caracteres.')
else:
    print('Você tem um nome com mais do que 6 caracteres.')
print()


"""
A função Len() totaliza a quantidade de caracteres e retorna um valor inteiro que pode
ser utilizado em operações como adições, subtrações...
"""
algo1 = str(input('Digite alguma coisa: '))
algo2 = str(input('Digite mais alguam coisa: '))

print(f'A quantidade total de caracteres digitados foi {len(algo1) + len(algo2)}')
print()
