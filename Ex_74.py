##074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

tupla = ()
maior = menor = 0
for i in range(5):
    numeros = random.randint(0,100)
    tupla = tupla + tuple([numeros])
print(f'Os números sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')



