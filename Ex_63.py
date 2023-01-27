#63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Ex: 0 - 1 - 1 - 2 - 3 - 5 – 8

n = int(input("Digite aqui qual o termo da Sequência de Fibonacci você quer descobrir:"))
c = 0
ultimotermo = 1
penultimotermo = 1
fibo = ultimotermo + penultimotermo


while c <= n:
    if c == 0 or c==1:
        print('1 ->', end='')
    elif c > 1:

        fibo = ultimotermo + penultimotermo
        penultimotermo = ultimotermo
        ultimotermo = fibo
        print('{}-> '.format(fibo), end='')
    c +=1

