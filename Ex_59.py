#059: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ]
# novos números [ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input("Digite aqui o primeiro valor:"))
num2 = int(input("Digite aqui o segundo valor:"))

print("OPERAÇÕES: \n [ 1 ] somar \n [ 2 ] multiplicar \n [ 3 ] maior \n [ 4 ] novos números \n [ 5 ] sair do programa \n")
menu = int(input("Digite qual opção você deseja realizar:"))

while menu !=5:
    if menu == 1:
        print(num1+num2)
        menu = int(input("Digite qual opção você deseja realizar:"))
    elif menu == 2:
        print(num1*num2)
        menu = int(input("Digite qual opção você deseja realizar:"))
    elif menu == 3:
        maior = 0
        if num1 > maior and num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        print("O maior numero é {}".format(maior))
        menu = int(input("Digite qual opção você deseja realizar:"))

    elif menu == 4:
        num1 = int(input("Digite aqui o primeiro valor:"))
        num2 = int(input("Digite aqui o segundo valor:"))
        menu = int(input("Digite qual opção você deseja realizar:"))
