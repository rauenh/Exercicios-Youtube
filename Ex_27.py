#27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite o nome completo: ")).upper().strip()
nome_lista = nome.split()
primeiro_nome = nome_lista[0]
ultimo_nome = nome_lista[-1]
print(nome_lista, primeiro_nome, ultimo_nome)
