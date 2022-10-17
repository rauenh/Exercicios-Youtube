# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan
angulo = float(input("Digite um angulo qualquer: "))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print("O valor do seno é {}, o valor de cosseno e {}, o valor de tangente é {}".format(seno, cosseno, tangente))