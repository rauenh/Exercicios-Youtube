#079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    menu = ' '
    valores_numericos = int(input("Digite um valor numérico: "))
    #lista.append(valores_numericos)
    if valores_numericos not in lista:
        lista.append(valores_numericos)
    else:
        print("Número repetido. Não será adicionado. ")
    while menu not in 'SN':
        menu = str(input("Deseja adicionar mais números? [S/N] :")).upper().strip()[0]
    if menu == 'N':
        break
lista.sort()
print(lista)