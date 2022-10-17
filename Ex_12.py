#Desafio 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input("Digite o preço do produto sem o desconto: "))
desconto = (((5/100)*preco)/1)
preco_desconto = preco - desconto

print("O valor do produto era {}, 5% do produto é {}, o desconto de 5% sobre o valor do produto foi {}".format(preco,desconto,preco_desconto))