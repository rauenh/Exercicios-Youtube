#25: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome completo:"))
nome_cortado = nome.title().split()
print(nome_cortado)
print("Seu nome tem Silva? {} ".format('Silva' in nome_cortado))



