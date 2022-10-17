# 22: Crie um programa que: a) leia o nome completo de uma pessoa b) mostre o nome
# com todas as letras maiúsculas c) com todas as minúsculas d) quantas letras ao
# todo (sem contar os espaços) e)  quantas letras tem o primeiro nome.

nome = str(input("Digite aqui o nome completo da pessoa:"))
print(nome)
print(nome.title())
print(nome.lower())
print(nome.upper())
print(len(nome.replace(" ","")))
nome_div= nome.split()
print(len(nome_div[0]))