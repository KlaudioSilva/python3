"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos
A palavra global faz uma variável do escopo externo ser
a mesma no escopo interno
"""

x = 1                       

def escopo():               #essa funcao não tem acesso a variaveis da funcao outra_funcao()
    global x
    x = 10                  #essa variável é de escopo LOCAL (ela só existe dentro dessa função)

    def outra_funcao():     #essa função tem acesso à funcao escopo()
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)                    #esse é o x GLOBAL
escopo()                    #chama a função que tem um x LOCAL
print(x)                    #o X é GLOBAL