#Desafio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode compar.

dinheiro = int(input("Digite quanto dinheiro você tem em sua carteira: "))
dolar = float(input("Digite a cotação do dólar hoje: "))

conversao = dinheiro/dolar

print("Você pode comprar {} dólares".format(conversao))