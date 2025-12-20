'''
Tipo tupla - Uma lista imutável
'''

#         0          1       2             3
#nomes =  'Klaudio', 'Elma', 'João Pedro', 'Arthur'   #assim cria-se uma tupla 
nomes = ('Klaudio', 'Elma', 'João Pedro', 'Arthur')  #usar parenteses também é um jeito de criar uma tupla 
print(nomes)        #exibe a tupla
   
#como converter uma tupla para uma lista:
nomes = list(nomes)
print(nomes)        #exibe a lista

#transformando a lista em uma tupla
nomes = tuple(nomes)
print(nomes[-1])    #exibe o último item da tupla
print(nomes)        #exibe a tupla completa

#tuplas são imutáveis
#nomes[2] = 'Otávio' #vai acontecer um erro, tuplas são imutáveis