#56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idademaior = 0
generomaior = 0
nomemaior = 0
quantidademulher = 0
somaidade = 0
for c in range (0,4):
    nome = str(input("Digite seu nome:\n"))
    idade = int(input("Digite sua idade:\n"))
    genero = str(input("Digite seu genero Masculino ou Feminino:\n"))

    if idade > idademaior:
        idademaior = idade
        nomemaior = nome
        generomaior = genero

    if genero == "feminino" and idade < 20:
        quantidademulher = quantidademulher +1

    somaidade = idade + somaidade
    mediaidade = somaidade/4

print("O nome da pessoa mais velha é {}, ela tem {} anos e seu gênero é {}".format(nomemaior,idademaior,generomaior))
print("A quantidade informada de mulheres abaixo de 20 anos é de {} pessoas.".format(quantidademulher))
print("A media das idades informadas é de {:.2f} anos".format(mediaidade))

