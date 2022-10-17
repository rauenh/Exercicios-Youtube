import random

a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno:"))
a3 = str(input("Digite o nome do terceiro aluno:"))
a4 = str(input("Digite o nome do quarto aluno: "))

lista = [a1, a2, a3, a4]

escolha1 = random.choice(lista)
escolha2 = random.choice(lista - escolha1)
escolha3 = random.choice(lista - escolha1 - escolha2)
escolha4 = random.choice(lista - escolha1 - escolha2 - escolha3)

print("O primeiro aluno escolhido foi {} o segundo aluno escolhido foi {} o terceiro aluno escolhido foi {} o quarto aluno escolhido foi {}".format(escolha1, escolha2, escolha3, escolha4))