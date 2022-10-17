#030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero_teste = int(input("Digite aqui um número:\n"))

if numero_teste%2 != 0:
    print("O número {} é ímpar".format(numero_teste))
else:
    print("O número {} é par".format(numero_teste))