"""
Pass e Ellipsis como placeholders.
Usamos o 'pass' ou '...' (ellipsis), quando queremos deixar um trecho/bloco de código vazio
e seguir para a próxima instrução, sem que isso cause um erro no código.

"""
# usando o pass
valor = False

if valor:
    # print('Oi')
    pass # acima comentei a instrução para usar o pass e demonstrar seu uso.
else:
    print('Tchau')
print()  # relembrando que estou usando o print só para pular uma linha


# usando ellipsis
if valor:
    # print('Oi')
    ...  # acima comentei a instrução para usar ... e demonstrar seu uso.
else:
    print('Tchau')
print()

"""
Tanto Pass como Ellipsis, fazem o interpretador do Python seguir com a leitura das
instruções do seu código sem que haja um erro de execução.
Geralmente os usamos quando não está definido o que aquele bloco de código irá fazer.
"""