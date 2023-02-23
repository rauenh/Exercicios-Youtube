palavras = ('azeite', 'macarrao', 'cadeira', 'colcha', 'pedra', 'madeira', 'mar', 'nuvens', 'aves', 'animais', 'borboleta', 'macaco', 'ovos', 'uva')
for n in palavras:
    print(f'\nA palavra {n.upper()} contém: ', end='' )
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')