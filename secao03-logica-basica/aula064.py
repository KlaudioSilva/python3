"""
Como gerar CPFs
"""

import random
import sys

print()

nove_digitos = ""
for i in range(9):
    nove_digitos += str(random.randint(0,9))

cont_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    #print(digito, cont_regressivo)
    resultado_digito_1 += int(digito) * cont_regressivo_1
    cont_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
#digito Recebe digito Se digito for Maior ou Igual a 9 Senão recebe 0
digito_1 = digito_1 if digito_1 <= 9 else 0

### trabalhando com o segundo digito do cpf
cont_regressivo_2 = 11
dez_digitos = nove_digitos + str(digito_1)

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * cont_regressivo_2
    cont_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(digito_1)
print(digito_2)

### Descobrindo se o cpf é válido
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado_pelo_calculo)
