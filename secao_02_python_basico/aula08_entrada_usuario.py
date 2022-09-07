"""
Entrada de dados do usuário com a função INPUT.
No Python e em outra liguagens, quando precisamos que o usuário passe ao programa 
algum tipo de dado, fazemos isso usando a função input(), que é literalmente 'entrada'
em inglês.
A função input() recebe como parâmetro uma string que será mostrada como auxílio ao usuário,
geralmente o informando que tipo de dado o programa espera receber.
Vejamos os exemplos:
"""
# o programa espera uma string
nome = str(input('Qual é o seu nome: '))

# o programa espera receber um número inteiro
numero = int(input('Digite um valor inteiro: '))

# o programa espera receber um número float
altura = float(input('Qual é a sua altura: '))

"""
Depois de fazermos isso, o terminal ira:
  → mostrar o texto (qual o nome, numero, altura e etc) na tela e
  aguardar até que o usuário digite o dado desejado.

Após a entrada dos dados pelo usuário, o programa irá continuar sua execução, passando
para as instruções seguintes.

Obs: se você não definir o tipo de dado esperado no input (str, int, float), o Python irá
entender essa entrada do usuário como uma string (mesmo que você digite um valor numérico).
Veja o exemplo.
"""
dado = input('Digite qualquer coisa aí: ')
print(dado, type(dado))
print()
