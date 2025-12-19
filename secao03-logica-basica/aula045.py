'''
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next     -> me entregue o próximo valor
iter     -> me entregue seu iterador
'''

#for letra in texto
texto = 'Klaudio'       #iterável
iterador = iter(texto)  #iterador


#o que o FOR faz por baixo dos panos
#while True:
#    try:
#        letra = next(iterador)
#        print(letra)
#    except StopIteration:
#        break

for letra in texto:
    print(letra)