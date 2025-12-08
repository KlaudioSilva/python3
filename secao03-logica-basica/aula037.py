"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 50:
    contador += 1

    if contador % 2 == 0:       #se o contador for PAR o número será ignorado
        print('--')
        continue

    print(contador)

print('Acabou a contagem que ignorou os números pares.')