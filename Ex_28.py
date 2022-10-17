#028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# descobrir qual foi o número escolhido pelo computador. -O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randrange

num_usuario = input("Digite um numero de 0 a 5\n")
num = randrange(0,5)
print(num)

if num_usuario == num:
    print("Você venceu!")
else:
    print("Você perdeu!")
