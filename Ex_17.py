#Desafio 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
catetoadjc = float(input("Digite a medida do cateto adjacente do triangulo retangulo:"))
catetoop = float(input("Digite a medida do cateto oposto do triangulo retangulo:"))
hipotenusa = math.hypot(catetoop,catetoadjc)

print("A hipotenusa é {:.2f}".format(hipotenusa))
