#Desafio 16 -  Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

numero = float(input("Digite um número qualquer: "))
truncado = math.trunc(numero)

print("a porção inteira do número é {}".format(truncado))