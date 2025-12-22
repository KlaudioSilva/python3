'''
split e join com list e str
split - divide uma string  'Fatia'
join  - une um string 'Concatena'
strip - limpa os espaços vazios
'''

frase = 'Olha só, que coisa mais interessante'
lista_frase = frase.split()
print(lista_frase)
lista_frase = frase.split(',')
print(lista_frase)
lista_frase = frase.split(' ')
print(lista_frase)
lista_frase = frase.split('mais')
print(lista_frase)
print('-' * 60)

frase2 = '    Que frase estranha   ,   tá tudo uma bagunça!'
lista_frase_crua = frase2.split(',')

lista_frases = []
for i, frase2 in enumerate(lista_frase_crua):
    lista_frases.append(lista_frase_crua[i].strip())

print(lista_frase_crua)
print(lista_frases)
print('-' * 60)

maius_minus = 'AaBbCcDdEd'
unindo = ' - '.join(maius_minus)
print(unindo)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)