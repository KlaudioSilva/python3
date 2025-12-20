'''
Introdução ao desempacotamento + tuplas (tuples)
'''

#usamos o asterisco '*' para criar uma lista com os itens ignorados
#                0          1       2             3
nome, *resto = ['Klaudio', 'Elma', 'João Pedro', 'Arthur']
print(nome, resto)      #exibe o nome escolhido e uma lista com os nomes ignorados

#usamos um sinal de underline '_' para ignorar valores que não serão mais usados
#                   0          1       2             3
_, nome, *resto = ['Klaudio', 'Elma', 'João Pedro', 'Arthur']
print(nome, resto)      #será exibido o segundo item na lista e o primeiro é totalmente ignorado

#                 0          1       2             3
_, _, nome, _ = ['Klaudio', 'Elma', 'João Pedro', 'Arthur']
print(nome)      #apenas o nome no índice 2 será preservado