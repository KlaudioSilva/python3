"""
Operação Ternária (condicional de uma linha)
    -basicamente um IF/ELSE em apenas uma linha
<valor> if <condição> else <outro valor>
"""
print()

condicao = 10 == 11     #se condição True 'Valor' senão 'Outro valor'
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

print('-' * 30)

digito = 9      # > 9 = 0
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('-' * 30)

print('Valor' if False else 'Outro valor' if False else 'Fim')      #possível fazer isso, mas não recomendável