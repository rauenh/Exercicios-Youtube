# 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from time import sleep
from random import randrange

print("=" * 60)
print(f"{' *** JOGO DO PAR OU ÍMPAR ***' : ^60}")
print("=" * 60)
ganhou = 0
while True:
    print("Computador: PAR ou ÍMPAR?")
    sleep(1)
    escolha = str(input("Usuário: ")).upper()
    print("Computador: Agora escolha um número de 0 a 10...")
    sleep(1)
    numero_usuario = int(input("Usuário: "))

    numero_comp = randrange(0, 10)
    print("Computador: Eu escolhi o número {}.".format(numero_comp))
    soma = numero_comp + numero_usuario

    if soma % 2 == 0:
        if escolha == 'PAR':
            ganhou += 1
            print("Usuário venceu!!! Vamos jogar novamente.")
            print("~" * 30)
            continue
        else:
            break
    else:
        if escolha == 'IMPAR':
            ganhou += 1
            print("Usuário venceu!!! Vamos jogar novamente.")
            print("~" * 30)
            continue
        else:
            break
print("Usuário perdeu com uma sequência de {} vitórias.".format(ganhou))
