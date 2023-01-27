#64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numeros = 0
soma = 0
c = 0

while numeros != 999:
    numeros = int(input("Digite aqui um numero:"))
    soma += numeros
    c += 1
    if numeros == 999:
        print("Finalizando")
        soma -= 999
        c-= 1
        break
print("A quantidade de números digitados foi {} e a soma entre eles foi de {}".format(c,soma))