'''
Repetições 
while
Executa uma ação enquanto uma condição for verdadeira
'''
qtd_linhas = 3
qtd_colunas = 3

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou!')