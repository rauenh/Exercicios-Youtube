#059: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ]
# novos números [ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input("Digite aqui o primeiro valor:"))
num2 = int(input("Digite aqui o segundo valor:"))
menu = 0
print(
    "OPERAÇÕES: \n [ 1 ] somar \n [ 2 ] multiplicar \n [ 3 ] maior \n [ 4 ] novos números \n [ 5 ] sair do programa \n")
menu = int(input("Digite qual opção você deseja realizar:"))
while menu !=5:
    if menu == 1:
        soma = num1 + num2
        print("A soma dos numeros {} e {} é de: {}".format(num1,num2, soma))
        menu = int(input("Digite qual opção você deseja realizar:"))
    elif menu == 2:
        produto = num1 * num2
        print("O produto dos números {} e {} é: {}".format(num1, num2, produto))
        menu = int(input("Digite qual opção você deseja realizar:"))
    elif menu == 3:
        maior = 0
        if num1 > maior and num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        print("O maior numero é {}".format(maior))
        menu = int(input("Digite qual opção você deseja realizar:"))

        #Dava para realizar da seguinte maneira:
        #if num1 >num2
        #maior = n1
        #else:
        #maior = n2
    elif menu == 4:
        num1 = int(input("Digite aqui o primeiro valor:"))
        num2 = int(input("Digite aqui o segundo valor:"))
        menu = int(input("Digite qual opção você deseja realizar:"))
    elif menu == 5:
        print("Finalizando o programa...")
    else:
        print("Opção inválida. Tente novamente.")
