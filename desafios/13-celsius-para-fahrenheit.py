#Escreva um programa que converta uma temperatura digita em Cº para Fº.
#fórmula = (25 °C × 9/5) + 32 = 77 °F

celsius = int(input('Digite uma temperatura em graus Cº: '))
fahren = int(celsius * 9/5) + 32

print('A temperatura de {}Cº convertida para Fahrenheit é igual a {}Fº'.format(celsius, fahren))