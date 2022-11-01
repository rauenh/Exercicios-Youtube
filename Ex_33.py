#033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))
num3 = int(input("Digite o terceiro número\n"))

if num3 >=num2 and num3 >= num1:
    maior = num3

else:
    if num2 >= num3 and num2 >= num1:
        maior = num2
    else:
        maior = num1


print("{} é maior".format(maior))

if num3 <= num2 and num3 <= num1:
    menor = num3

else:
    if num2 <= num3 and num2 <= num1:
        menor = num2
    else:
        menor = num1

print("{} é o menor".format(menor))

