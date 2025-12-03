#Escreva um programa que leia um valor em metros e exiba convertido, em centímetros e milímetros

metros = float(input('Digite uma distância em metros: '))
centimetros = metros / 100
milimetros = metros / 1000

print('A distância {}m, em centímetros é: {} e em milímetros é: {}'.format(metros, centimetros, milimetros))