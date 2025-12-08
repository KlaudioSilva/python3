''' while/else '''
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':    #se existir um espaço dentro da string
        break           #se o break for executado, o else NÂO será executado

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string')

print('Fora do while')