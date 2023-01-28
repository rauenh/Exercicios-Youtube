#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = 0
maior = 0
menor = 0
c = 0
numeros = 0
soma = 0
menu = str(input("Você quer digitar mais valores? [S/N]")).upper()
while menu != 'N':
    numeros = int(input("Digite aqui um número:"))
    menu = str(input("Você quer digitar mais valores? [S/N]")).upper()
    soma += numeros
    if numeros > maior:
        maior = numeros
    elif maior > numeros:
        menor = numeros
    elif numeros < menor:
        menor = numeros
    c += 1
if menu == 'N':
    media = soma/c
print("Foram digitados {} números. O maior número foi {}, o menor número foi {} e a média entre todos os números digitados é de {}".format(c,maior,menor,media))