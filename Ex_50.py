#50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(0,6):
    numeros = int(input("Digite aqui um numero inteiro:"))
    if numeros%2 == 0:
        soma = soma + numeros
        cont = cont + 1
print("A soma dos {} numeros pares informados é {}".format(cont, soma))