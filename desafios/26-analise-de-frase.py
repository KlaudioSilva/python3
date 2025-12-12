'''
Faça um programa que leia uma frase pelo teclado e mostre:
 - quantas vezes aparece a letra "a"
 - em que posição ela aparece a primeira vez
 - em que posição ela aparece a última vez
 '''

print('-' * 30)
print(f'{"Analisando Uma Frase":^30}')
print('-' * 30)

text = str(input('Digite uma frase para ser analisada: ')).lower()
letra = str(input('Escolha a letra que será contada: ')).lower()

qtd_aparece = text.count(letra)     #contagem de aparições da letra escolhida

print('Por enquanto estamos ignorando letras acentuadas na contagem:')
print(f'A letra "{letra}" apareceu {qtd_aparece} vezes na frase.')

posicao = text.find(letra)          #posição no index onde a letra aparece pela primeira vez

print(f'A posição em que a "{letra}" apareceu a primeira vez: {posicao}')

ultima = text.rfind(letra)

print(f'A última vez que a letra "{letra}" aparece no texto é na posição: {ultima}')