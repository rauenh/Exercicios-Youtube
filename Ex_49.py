#49: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Digite um número: "))
for c in range(1,11):
    tabuada = numero*c
    print("{} * {} = {} ".format(c,numero, tabuada))

