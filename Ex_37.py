#37: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite aqui um numero inteiro qualquer:\n"))

menu = int(str(input("Digite 1 para converter em binario, 2 para converter em hexadecimal ou 3 para converter em octal\n")))

if menu == 1:
    divisao1 = numero//2
    resto1 = numero%2
    divisao2 = divisao1//2
    resto2 = divisao1%2
    divisao3 = divisao2//2
    resto3 = divisao2%2
    divisao4 = divisao3//2
    resto4 = divisao3%2
    divisao5 = divisao4//2
    resto5 = divisao4%2

    print("O numero convertido é {}{}{}{}{}{}".format(divisao5,resto5,resto4,resto3,resto2,resto1))

elif menu == 2:
    divisao1 = numero//16
    resto1 = numero%16
    divisao2 = divisao1//16
    resto2 = divisao1%16
    divisao3 = divisao2//16
    resto3 = divisao2%16
    divisao4 = divisao3//16
    resto4 = divisao3%16

    print("O numero convertido é {}{}{}{}{}".format(divisao4, resto4,resto3, resto2,resto1))

else:
    divisao1 = numero // 8
    resto1 = numero % 8
    divisao2 = divisao1 // 8
    resto2 = divisao1 % 8
    divisao3 = divisao2 // 8
    resto3 = divisao2 % 8
    divisao4 = divisao3 // 8
    resto4 = divisao3 % 8

    print("O numero convertido é {}{}{}{}{}".format(divisao4, resto4,resto3, resto2,resto1))

