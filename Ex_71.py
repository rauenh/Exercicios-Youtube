# 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('*-' * 20)
print('{:-^40}'.format(' BANCO CAI$HA '))
print('*-' * 20)
cedulas_50 = resto_50 = cedulas_20 = resto_20 = cedulas_10 = resto_10 = cedulas_1 = resto_1 = 0
while True:
    valor = int(input("Digite aqui o valor a ser sacado: R$"))
    if valor//50 != 0:
        cedulas_50 = valor // 50
        resto_50 = valor%50
        cedulas_20 = resto_50//20
        resto_20 = resto_50%20
        cedulas_10 = resto_20//10
        resto_10 = resto_20%10
        cedulas_1 = resto_10//1
        print(f'Você poderá sacar com {cedulas_50} cédulas de 50 reais, {cedulas_20} cédulas de 20 reais, {cedulas_10} cédulas de 10 reais e {cedulas_1} cédulas de 1 real.')
    elif valor//20 != 0:
        cedulas_20 = valor // 20
        resto_20 = valor % 20
        cedulas_10 = resto_20 // 10
        resto_10 = resto_20 % 10
        cedulas_1 = resto_10 // 1
        print(f'Você poderá sacar com {cedulas_20} cédulas de 20 reais, {cedulas_10} cédulas de 10 reais e {cedulas_1} cédulas de 1 real.')
    elif valor//10 != 0:
        cedulas_10 = valor// 10
        resto_10 = valor% 10
        cedulas_1 = resto_10 // 1
    else:
        cedulas_1 = valor//1
        print(f'Você poderá sacar com {cedulas_1} cédulas de 1 real.')
    menu = ' '
    while menu not in 'SN':
        menu = str(input("Deseja realizar outra operação? [S/N] ")).upper().strip()[0]
    if menu == 'N':
        break
print('*-' * 20)
print("O banco CAI$HA agradece. Volte sempre!")
print('*-' * 20)
