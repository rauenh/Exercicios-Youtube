# 032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input("Digite qualquer ano no formato YYYY\n"))

if ano % 400 == 0 or ano % 4 == 0:
    print("É um ano bissexto")
else:
    print("Não é bissexto")
