#Crie um programa que leia um número inteiro e mostre seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número inteiro qualquer: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print('O dobro de', num, 'é', dobro)
print('O triplo de', num, 'é', triplo)
print('A raiz quadrada de', num, 'é', raiz)