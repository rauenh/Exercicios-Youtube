#080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista_desordenada = []
c =  0
while c < 5:
    valores_numericos = int(input("Digite aqui um valor numérico:" ))
    lista_desordenada.append(valores_numericos)
    c += 1
    for posicao in range(len(lista_desordenada)):
        if valores_numericos < lista_desordenada[posicao]:
            lista_desordenada.insert(posicao, valores_numericos)
            lista_desordenada.pop()
            break


    # print(lista_desordenada.index(elementos)) #se ele encontra um elemento repetido ele printa a posição da primeira ocorrencia do elemento

print(lista_desordenada)



