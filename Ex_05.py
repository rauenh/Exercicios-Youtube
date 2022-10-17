#Desafio 05 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero=int(input("Digite um número: "))
antecessor = None
sucessor = None

if antecessor is None and sucessor is None:
    antecessor = numero - 1
    sucessor = numero + 1

print("O antecessor do número {} digitado é {} e o seu sucessor é {}".format(numero , antecessor , sucessor))
