##029: Escreva um programa que leia a velocidade de um carro.
# -Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado.
# -A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Digite a velocidade do carro:\n"))

if velocidade > 80:
    excedeu = velocidade - 80
    multa = excedeu*7
    print("Você excedeu {} km do limite permitido. Você foi multado. O valor da sua multa é R$ {} ".format(excedeu, multa))

else:
    print("Parabéns, você está no limite da velocidade")