'''
Em python é possível editar, fatiar, mudar, trocar e outras coisas com strings
'''
#        0123456789
frase = 'Curso em vídeo de Python'
print(frase[5:9])       #inicia do indice 5 e vai até o indice 8 (o 9 será ignorado)
print(frase[5:9:2])     #do 5 até o 8, pulando de dois em dois
print(frase[5:])        #do 5 até o final da string (texto)
print(frase[:5])        #do indice 0 até o 5
print(frase[5::3])      #do 5 até o final pulando de tres em tres
print('-' * 30)

print(f'Comprimento do texto: {len(frase)}')
print(f'Quantas vezes a letra "o" apareceu na frase: {frase.count("o")}')
print('-' * 30)

print(f'De minúscula para maiúscula e localizar a posição: {frase.upper()}')
print(f'Localizar a posição: {frase.find("vídeo")}')
print(f'Trocar palavras: {frase.replace("Python", "Android")}')