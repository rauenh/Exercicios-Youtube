##57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
genero = 1

while genero != 0:
    genero = str(input("Digite aqui seu gênero [M/F]:")).upper()
    if genero == 'F' or genero == 'M':
        print("Gênero {} registrado com sucesso".format(genero))
        break
    else:
        print("Digite uma opção valida")