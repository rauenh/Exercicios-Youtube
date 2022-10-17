# Desafio 08 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = int(input("Digite o valor em metros:"))
cmetros = valor*100
cmilimetros = valor*1000

print("O valor digitado foi {}m, que em centimetros equivale a {}cm e em milímetros equivale a {}mm".format(valor, cmetros, cmilimetros))