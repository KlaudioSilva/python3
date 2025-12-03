#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Qual é a largura da parede em metros: '))
altura = float(input('Qual é a altura da parede em metros: '))
area = largura * altura

tot_tinta = area / 2

print('A área de uma parede de largura={}m e altura={}m, é={}m²'.format(largura, altura, area))
print('Como cada litro de tinta pinta 2m², você vai gastar {}l de tinta para pintar essa parede.'.format(tot_tinta))