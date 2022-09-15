"""
While / Else
Contadores
Acumuladores
Ao final do while podemos utilizar a instrução 'else'. O propósito disso é 
executar alguma instrução ou bloco de código ao final do laço 'while'.

No laços 'while', a expressão é testada enquanto for verdadeira. A partir 
do momento que ela se torna falsa, o código da cláusula 'else' será 
executado, se estiver presente.
"""
x = 0
while x < 10:
    print(x)
    x += 1
else:
    print('Fim do while')
print()

"""
Se dentro da repetição for executado um break, o loop será encerrado sem executar
o conjunto da cláusula else.
Veja o exemplo:
"""
x = 1
while x <= 10:
    print(x)
    x += 1
    # se o x for igual a 6 termine a execução
    if x == 6:
        print('X é igual a 6')
        break
else:
    print('Fim do while.')
print()

# usando acumuladores
cont = 1
acum = 1

while cont <= 10:
    print(f'Contador → {cont}, acumulador → {acum}')

    acum = acum + cont
    cont += 1
else:
    print('Cheguei no else.')
print()