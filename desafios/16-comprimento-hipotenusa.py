'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
'''
import math
print('-' * 3, 'Qual é o comprimento da Hipotenusa', '-' * 3)

cat_oposto = int(input('Digite o comprimento do Cateto Oposto: '))
cat_adjcente = int(input('Digite o comprimento do Cateto Adjacente: '))

cat_oposto_pot = pow(cat_oposto, 2)
cat_adjcente_pot = pow(cat_adjcente, 2)

soma_catetos = (cat_oposto_pot + cat_adjcente_pot)

comp_hipotenusa = math.sqrt(soma_catetos)

print(f'O comprimento da Hipotenusa de um triângulo retângulo com catetos de {cat_oposto} e {cat_adjcente} é igual a: {comp_hipotenusa}.')