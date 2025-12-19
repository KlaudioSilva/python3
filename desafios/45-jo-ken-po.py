'''
Crie um programa que faça o computador jogar JOKENPÔ com você.
'''

#importando bibliotecas necessárias
import time, random


print('\n')
print('\033[92m-\033[m' * 30)
print(f'\033[91m{"JOGANDO JOKENPÔ":^30}\033[m')
print('\033[92m-\033[m' * 30)

#print('\033[96m=\033[m' * 12, f'\033[94m{"PYTHON"}\033[m', '\033[96m=\033[m' * 12)

print('''
Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

itens = ['Pedra', 'Papel', 'Tesoura']              #lista com as opções
opcao = int(input('Qual é a sua jogada? '))        #escolha do jogador
sorteado = random.randint(0, 2)                    #escolha do computador

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!')

print('-=' * 11 + '-')
print('Computador jogou {}'.format(itens[sorteado]))
print('Jogador jogou {}'.format(itens[opcao]))
print('-=' * 11 + '-')

if sorteado == 0:       #computador jogou PEDRA
    if opcao == 0:
        print('EMPATE')
    elif opcao == 1:
        print('\033[94mJOGADOR VENCE\033[m')
    elif opcao == 2:
        print('\033[33mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[33mJOGADA INVÁLIDA!\033[m')
elif sorteado == 1:     #computador jogou PAPEL
    if opcao == 0:
        print('\033[33mCOMPUTADOR VENCE\033[m')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('\033[94mJOGADOR VENCE\033[m')
    else:
        print('\033[33mJOGADA INVÁLIDA!\033[m')
elif sorteado == 2:     #computador jogou TESOURA
    if opcao == 0:
        print('\033[94mJOGADOR VENCE\033[m')
    elif opcao == 1:
        print('\033[33mCOMPUTADOR VENCE\033[m')
    elif opcao == 2:
        print('EMPATE')
    else:
        print('\033[33mJOGADA INVÁLIDA!\033[m')