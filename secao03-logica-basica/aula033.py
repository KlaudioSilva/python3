"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Tipos que são Imutáveis que vimos: str, int, float, bool
"""

string = 'Klaudio Silva'
outra_variavel = f'{string[:3]}W{string[4:]}'

tudo_maiuscula = str.upper(string)          #aplicando em uma nova variável

print(string)
print(outra_variavel)

print(tudo_maiuscula)
print(string.lower())                       #aplicando diretamente no print