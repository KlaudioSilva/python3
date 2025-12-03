#Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
dia = input('Em que dia você nasceu: ')
mes = input('Qual é o mês de seu nascimento: ')
ano = input('Em que ano você nasceu: ')
print('\n')

print('Primeiro estilo de data formatada.')
print('----------------------------------')
print('Você nasceu no dia', dia, 'do mês', mes, 'do ano de', ano)
print('\n')

print('Segundo estilo de data formatada.')
print('----------------------------------')
print('A sua da de nascimento é', dia + '/' + mes + '/' + ano)