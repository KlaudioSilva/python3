"""
Crie um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos exiba a mensagem: "Seu nome é curto"; se tiver entre 5 e 6 letras, exiba
"Seu nome é normal"; se tiver mais do que 6 letras, "Seu nome é muito grande".
"""
print('-' * 30)
print('O TAMANHO DO SEU NOME'.center(30))
print('-' * 30)
print()

nome = str(input('Digite o seu primeiro nome: '))

# nome curto
if len(nome) <= 4:
    print('Seu nome é curto.')

# nome normal
elif (len(nome) >= 5) and (len(nome) <= 6):
    print('Seu nome é normal.')

# nome grande
else:
    print('Seu nome é bem grande.')
print()

print('-' * 30)
print('Fim do programa. Obrigado e volte sempre!')
print()
