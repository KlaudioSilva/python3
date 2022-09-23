"""
Validando um CPF

CPF = 168.995.350-09
--------------------------------------------
1 * 10 = 10            #     1 * 11 = 11 ←
6 *  9 = 54            #     6 * 10 = 60
8 *  8 = 64            #     8 *  9 = 72
9 *  7 = 63            #     9 *  8 = 72
9 *  6 = 54            #     9 *  7 = 63
5 *  5 = 25            #     5 *  6 = 30
3 *  4 = 12            #     3 *  5 = 15
5 *  3 = 15            #     5 *  4 = 20
0 *  2 =  0            #     0 *  3 =  0
                       #  →  0 *  2 =  0
           297         #                343
11 - (297 % 11) = 11   #     11 - (343 % 11) = 9
11 > = 0               #
Digito 1 = 0           #     Digito 2 = 9
"""
from turtle import st


print('+-' * 15 + '+')
print(f'{"VALIDANDO CPF":^31}')
print('+-' * 15 + '+')

# novo cpf
cpf = input('Digite um CPF: ')
qtd_digitos = len(cpf)

if not cpf.isnumeric():
    print('CPF Inválido! Digite apenas números.')
elif not qtd_digitos == 11:
    print('CPF Inválido! Quantidade inválida de digitos.')
else:
    verifica_cpf = list(cpf[:9])
    result_cpf = cpf[9:]

# primeiro digito
d1, d2, d3, d4, d5, d6, d7, d8, d9 = verifica_cpf
val1 = int(d1) * 10
val2 = int(d2) * 9
val3 = int(d3) * 8
val4 = int(d4) * 7
val5 = int(d5) * 6
val6 = int(d6) * 5
val7 = int(d7) * 4
val8 = int(d8) * 3
val9 = int(d9) * 2

tot_digt_1 = val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8 + val9
print(tot_digt_1)

# encontrando o primeiro digito
digito_1 = 11 - (tot_digt_1 % 11)
if digito_1 > 9:
    digito_1 = 0
    print(digito_1)
print(digito_1)

# segundo digito
d1, d2, d3, d4, d5, d6, d7, d8, d9 = verifica_cpf
val1 = int(d1) * 11
val2 = int(d2) * 10
val3 = int(d3) * 9
val4 = int(d4) * 8
val5 = int(d5) * 7
val6 = int(d6) * 6
val7 = int(d7) * 5
val8 = int(d8) * 4
val9 = int(d9) * 3
val10 = digito_1 * 2

tot_digt_2 = val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8 + val9 + val10
print(tot_digt_2)

# encontrando o segundo digito
digito_2 = 11 - (tot_digt_2 % 11)
if digito_2 > 9:
    digito_2 = 0
print(digito_2)

# validando cpf
novo_cpf = cpf[:9] + str(digito_1) + str(digito_2)
if novo_cpf == cpf:
    print(f'O CPF {novo_cpf} foi validado com sucesso.')
else:
    print(f'O CPF {novo_cpf} é inválido.')
print()

"""
Resposta do Desafio:
while True:
    # cpf = '16728893830'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range (0, 19):
        if index > 8:
            index -= 9
        
        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11

            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
            total = 0
            novo_cpf += str(digito)

    # Evita sequencias. ex: 11111111111, 00000000000
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)


    if cpf == novo_cpf and not sequencia:
        print('Válido!')
    else:
        print('Inválido!')
"""