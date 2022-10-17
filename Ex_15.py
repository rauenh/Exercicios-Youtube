#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
#  dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Digite aqui a quantidade de km percorridos: "))
dias = int(input("Digite aqui a quantidade de dias que o carro foi alugado: "))
preco = dias*60 + km*(0.15)

print("O preço a pagar é de {}, o carro ficou alugado durante {} dias e foi usado por {} kms".format(preco, dias, km))