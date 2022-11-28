# 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
jogador = int(input(''' Escolha pedra, papel ou tesoura:
1 - Pedra
2 - papel
3 - tesoura
Digite uma opção: \n'''))

computador = randint(1,3)

if jogador == computador:
    print("Empate, jogar novamente")
elif jogador == 1 and computador == 3:
    print("Vc venceu, o computador jogou {} tesoura. Pedra esmaga tesoura.".format(computador))
elif jogador == 3 and computador == 1:
    print("Vc perdeu, o computador jogou {} pedra. Pedra esmaga tesoura.".format(computador))
elif jogador == 2 and computador == 3:
    print("Vc perdeu, o computador jogou {} tesoura. Tesoura corta papel.".format(computador))
elif jogador == 3 and computador == 2:
    print("Vc ganhou, o computador jogou {} papel. Tesoura corta papel.".format(computador))
elif jogador == 2 and computador == 1:
    print("Vc ganhou. O computador jogou {}, papel embrulha pedra.".format(computador))
elif jogador == 1 and computador == 2:
    print("Vc perdeu, o computador jogou {}. Papel embrulha pedra".format(computador))
else:
    print("escolha uma opçao valida")

