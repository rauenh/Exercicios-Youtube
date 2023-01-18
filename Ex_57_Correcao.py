genero = str(input("Digite aqui seu gênero [M/F]:")).strip().upper()[0]

while genero not in 'MmfF':
    genero = str(input("Dados inválidos. Digite seu genero:")).strip().upper()[0]
    print("Genero {} registrado com sucesso".format(genero))