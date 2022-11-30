#52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite aqui um numero inteiro maior que 1:\n"))

if  numero%1 == 0 and numero%numero == 0:
    print(numero%numero)
    print("O número {} é um número primo".format(numero))
#else:
    #print("O número {} não é um numero primo".format(numero))
