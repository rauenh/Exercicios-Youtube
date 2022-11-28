# 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print("-="*10)
itens=('Pedra', 'Papel', 'Tesoura')
jogador = int(input(''' Escolha pedra, papel ou tesoura:
0 - Pedra
1 - papel
2 - tesoura
Digite uma opção: \n'''))
if jogador >=3:
    print("Opção invalida")


computador = randint(0,2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print("Você escolheu {}".format(itens[jogador]))
print("O computador escolheu {}".format(itens[computador]))
print("-="*10)
if jogador == computador:
    print("Empate, jogar novamente")
elif jogador == 0 and computador == 2:
    print("Vc ganhou, o computador jogou {} tesoura. Pedra esmaga tesoura.".format(computador))
elif jogador == 2 and computador == 0:
    print("Vc perdeu, o computador jogou {} pedra. Pedra esmaga tesoura.".format(computador))
elif jogador == 1 and computador == 2:
    print("Vc perdeu, o computador jogou {} tesoura. Tesoura corta papel.".format(computador))
elif jogador == 2 and computador == 1:
    print("Vc ganhou, o computador jogou {} papel. Tesoura corta papel.".format(computador))
elif jogador == 1 and computador == 0:
    print("Vc ganhou. O computador jogou {}, papel embrulha pedra.".format(computador))
elif jogador == 0 and computador == 1:
    print("Vc perdeu, o computador jogou {}. Papel embrulha pedra".format(computador))

