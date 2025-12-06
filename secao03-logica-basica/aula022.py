# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São consideradas falsy:
# 0 - 0.0 - '' - False --> ou seja: zero, zero ponto zero, string vazia (sem espaço) ou False mesmo.
# Também existe o tipo None que é usado para representar um Não valor.

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if(entrada == 'E' or entrada == 'e)' and senha_digitada == senha_permitida):
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True or False or True)

print(False and True and True)

senha2 = input('Nova senha: ') or 'Nenhuma senha digitada!'
print(senha2)