#60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num1 = int(input("Digite aqui um número inteiro qualquer:"))
num = 1
fatorial = 1
print("O fatorial deste número será:")

while num1 != 1:
    fatorial = fatorial*num1
    num1 = num1 - 1
    print(fatorial)

