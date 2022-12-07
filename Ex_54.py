#54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date
from datetime import date
atual = date.today().year
maioridade = 0
for c in range (0,8):
    nascimento = int(input("Digite aqui o ano do seu nascimento:\n"))
    compara = atual - nascimento
    if compara >= 18:
        maioridade = maioridade + 1

print("A quantidade de pessoas que atingiram a maioridade são {}".format(maioridade))

