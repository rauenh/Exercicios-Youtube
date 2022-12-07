#55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range (0,6):
    peso = float(input("Digite aqui seu peso em kgs:\n"))
    if peso > maior :
        maior = peso
    elif maior > peso:
        menor = peso
    elif peso < menor:
        menor = peso
print("O maior peso lido foi {} kg, o menor peso lido foi {} kg.".format(maior,menor))