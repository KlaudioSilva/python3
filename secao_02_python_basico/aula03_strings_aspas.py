"""
Strings é um tipo de dados primitivos no Python.
Uma string é um texto, palavra ou caracter que está dentro de aspas.
str → string
"""
print('String com aspas simples')
print("String com aspas duplas")


"""
Se dentro de uma string for necessário usarmos aspas simples ou duplas, pode ocorrer um
erro se não prestamos atenção.
Para solucionar o problemas fazemos: se dentro da string vamos usar aspas simples, então
abrimos e fechamos a string com as duplas.
Se queremos usar aspas duplas dentro da string, então abrimos e fechamos a string com
aspas triplas. Veja o exemplo:
"""
print("Essa é uma 'string' (str).")
print('Mesmo exemplo de "string" (str).')
print("""Temos aqui outra "string" (str).""")
print()

"""
Outra forma de evitar erros no uso de aspas dentro de strings é usar a
barra invertida '\' antes das aspas. A barra invertida é conhecida como
caracter de escape. Veja o exemplo:
"""
print('Esse é o meu \"texto\" (str).')
print("Esse é o meu \'texto\' (str).")

# Obs. sempre que puder evite usar a barra invertida assim, porque o seu código pode ficar confuso e díficl de ler

