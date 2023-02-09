#69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

print('*='*20)
print(f"{' *** CADASTRO DE USUÁRIOS ***' : ^40}")
print('*='*20)
maioridade = masculino = feminino = menu = 0
while menu != 'N':
    nome = str(input("Digite aqui o nome da pessoa:"))
    idade = int(input("Digite aqui a idade:"))
    sexo = str(input("Digite aqui o gênero (M/F): ")).upper().strip()[0]
    menu = str(input("Deseja continuar? (S/N):")).upper().strip()[0]
    if sexo =='M':
        masculino += 1
    if idade > 18:
        maioridade += 1
    if sexo =='F' and idade < 20:
        feminino += 1
    if menu == 'N':
        break
print("PROGRAMA FINALIZADO COM SUCESSO!")
print("Aqui estão as informações:\n")
print("Foram cadastradas {} pessoas com mais de 18 anos.".format(maioridade))
print("Foram cadastrados {} pessoas do gênero masculino.".format(masculino))
print("Foram cadastrados {} pessoas do gênero feminino abaixo de 20 anos de idade".format(feminino))