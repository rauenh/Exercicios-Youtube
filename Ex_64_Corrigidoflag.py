numeros = 0
soma = 0
c = 0
numeros = int(input("Digite aqui um numero:"))
while numeros != 999:
    soma += numeros
    c += 1
    numeros = int(input("Digite aqui um numero:"))
print("A quantidade de números digitados foi {} e a soma entre eles foi de {}".format(c,soma))
