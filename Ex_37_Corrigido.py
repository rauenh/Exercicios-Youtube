numero = int(input("Digite aqui um número inteiro qualquer:\n"))
print('''Escolha uma das bases a seguir para conversão:
1 - Converte para Binário
2 - Converte para Octal
3 - Converte para Hexadecimal''')
menu = int(input("Digite aqui o número da sua opção:\n"))
if menu ==1:
    print("O número {} convertido para a base binária é {}".format(numero, bin(numero)[2:]))
elif menu ==2:
    print("O número {} convertido para a base octal é {}".format(numero,oct(numero)[2:]))
elif menu ==3:
    print("O número {} convertido para a base hexadecimal é {}".format(numero,hex(numero)[2:]))
else:
    print("Digite uma opção válida")