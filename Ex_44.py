#44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal - 3x ou mais no cartão: 20% de juros

preco = float(input("Digite aqui o preço do produto em reais:\n"))
menu = int(input('''Opções de pagamento:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros\n
Qual opção deseja?'''))

if menu == 1:
    desconto = (10*preco)/100
    valor = preco - desconto
    print("Você irá pagar {:.2f}, o desconto foi de {:.2f}.".format(valor,desconto))

elif menu ==2:
    desconto = (5 * preco) / 100
    valor = preco - desconto
    print("Você irá pagar {:.2f}, o desconto foi de {:.2f}.".format(valor, desconto))

elif menu ==3:
    parcelas = preco/2
    print("Você irá pagar duas parcelas de {:.2f}. Não há desconto nessa modalidade".format(parcelas))

elif menu ==4:
    quantidade= int(input("Quantas parcelas?"))
    juros = (20*preco)/100
    valor = preco + juros
    parcelas = preco/quantidade
    print("Você irá pagar no total {:.2f} pelo produto. Será {} parcelas de {:.2f} reais cada. Teve um acrescimo de {:.2f} reais no valor final do produto.".format(valor,quantidade, parcelas,juros))
else:
    print("Digite uma opção válida")