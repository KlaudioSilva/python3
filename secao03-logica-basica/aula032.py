'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
print('-' * 5, 'PAR ou ÍMPAR', '-' * 5)
num = (input('Digite um número inteiro: '))

if num.isdigit():

    num_int = int(num)
    if num_int % 2 == 0:
        print(f'O número {num} é PAR!')
    else:
        print(f'O número {num} é ÍMPAR!')

else:
    print('Você não digitou um número inteiro')
    

print('\n')
'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
'''
print('-' * 5, 'SAUDAÇÕES', '-' * 5)
hora = input('Que horas são? ')

try:
    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora.')
except:
    print('Por favor, digite apenas números inteiros.')


print('\n')
'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva:
"Seu nome é curto"; se tiver entre 5 e 6 letras, escreva: "Seu nome é normal"; maior do que 6
letras, escreva: "Seu nome é muito grande".
'''
print('-' * 5, 'TAMANHO NOMES', '-' * 5)
nome = input('Digite o seu nome: ')

nome_tam = len(nome)

if nome_tam == 0:
    print('Você não digitou seu nome:')
elif nome_tam <= 4:
    print('Seu nome é curto')
elif nome_tam <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande!')