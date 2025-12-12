'''
Crie um programa que escolha um número de 0 a 5 e faça o usuário
tentar descobrir qual foi o escolhido pelo programa.
Na tela deverá aparecer se o usuário venceu ou perdeu.
'''

import random
print('-' * 30)
print(f'{"Jogo: ADIVINHE O NÚMERO":^30}')
print('-' * 30)

num_sorteio = random.randint(0, 5)      #sorteia números inteiros entre 0 e 5
chances = 0

for c in range(0, 3):                   #loop das chances de chute
    
    chute = int(input(f'{c+1}ª Tentativa: '))

    if chute == num_sorteio:            #se acertar o número que está na variável:
        print(f'* * Você chutou "{chute}" e acertou o número na {c+1}º tentativa. Parabéns! * *')
        break

    if c >= 2:                          #Não acertou o número em nenhum dos chutes
        print('-- Você gastou todos os seus chutes. Melhor sorte na próxima. --')
    
print('-+' * 14 + '-')
print('Jogue Novamente')