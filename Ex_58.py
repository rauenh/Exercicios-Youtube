#58: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randrange

num_usuario = int(input("Digite um numero de 0 a 10\n"))
num = randrange(0,10)

tentativas = 0

while num_usuario != num:
    print("Tente novamente!")
    num_usuario = int(input("Digite um numero de 0 a 10\n"))
    tentativas += 1

if num_usuario == num:
    print("Você acertou! Foram necessárias {} tentativas para acertar. Parabéns!".format(tentativas))
