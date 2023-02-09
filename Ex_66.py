#66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# , que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

inteiro = int(input("Digite aqui um número inteiro positivo: "))
cont = soma = 0

while True:
    inteiro = int(input("Digite aqui um número inteiro positivo: "))
    if inteiro == 999:
        break
    soma += inteiro
    cont += 1
print(f'Foram digitados {cont} números. A soma entre eles é de {soma}')