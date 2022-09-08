"""
Condicionais IF, ELIF e ELSE
Quando precisamos decidir alguma coisa no programa podemos usar
condicionais. Se uma condição é atendida então é executado aquele
bloco de código 'se' a condição não é atendida o programa segue para o
próximo bloco e 'se' aquela condição for atendida então é executada a instrução.
Ou seja: se uma condição é Verdadeira ela executa-se a instrução, senão o programa segue para
a próxima condição.
Podemos dizer que as condições IF, ELIF e ELSE, significam literalmente: SE, SENÃO SE e SENÃO.
"""

# se a instrução for verdadeira, ela será executada
if False:
    print('Verdadeiro.')
    print('Olá')
# se a instrução acima for falsa a próxima será executada
elif False:
    print('Agora é verdadeiro.')
    print('Oi agora sou eu.')
# se nenhuma das instruções anteriores for verdadeira o instrução do ELSE será executada
else:
    print('Não é verdadeiro.')
    print('Parece que nenhuma das anteriores era verdadeira.')

# se nenhuma das instruções for atendidas o programa não executa nada.
# Atenção, cada bloco condicional deve estar devidamente identado:
# if NonoNon:
#     NonoNon
# else:
#     No Non On