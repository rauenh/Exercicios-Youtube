#67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print("="*60)
print(f"{' *** TABUADA ***' : ^60}")
print("="*60)
numero = int(input("Qual o número que você deseja saber a tabuada? Digite a seguir: "))
cont = 0
while numero > 0:
    for c in range(1, 11):
        tabuada = numero * c
        print("{} * {} = {} ".format(c, numero, tabuada))
        cont += 1
    numero = int(input("Qual o número que você deseja saber a tabuada? Digite a seguir: "))
    if numero < 0:
        break
print("="*60)
print(f"{' *** TABUADA FINALIZADA COM SUCESSO ***' : ^60}")
print("="*60)