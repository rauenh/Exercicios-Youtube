listanum = []
maior = menor = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        meior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}, o maior valor foi {maior}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i} ...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ',end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')