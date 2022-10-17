#031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input("Digite a distância da viagem em Km\n"))

if distancia > 200:
    valor1 = distancia*0.45
    print("O valor da passagem será de {}".format(valor1))
else:
    valor2 = distancia*0.50
    print("O valor da passagem será de {}".format(valor2))

