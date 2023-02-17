from random import randint

# n = (randint(1,10)) #colocar dentro de dois parenteses já a torna uma variável composta
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os numeros sorteados foram {n}')
for c in n:
    print(f'{c} ',end='')

print(f'\nO maior valor sorteado foi {max(n)}')
print(f'\nO menor valor sorteado foi {min(n)}')