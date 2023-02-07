#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = maior = menor = c = numeros = soma = 0
menu = 'S'
while menu != 'N':
    numeros = int(input("Digite aqui um número:"))
    soma += numeros
    c += 1
    if c == 1:
        maior = menor = numeros
    elif numeros > maior:
        maior = numeros
    elif numeros < menor:
        menor = numeros
    menu = str(input("Você quer digitar mais valores? [S/N]")).upper()
if menu == 'N':
    media = soma/c
print("Foram digitados {} números. O maior número foi {}, o menor número foi {} e a média entre todos os números digitados é de {}".format(c,maior,menor,media))