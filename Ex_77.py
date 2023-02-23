#077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('azeite', 'macarrao', 'cadeira', 'colcha', 'pedra', 'madeira', 'mar', 'nuvens', 'aves', 'animais', 'borboleta', 'macaco', 'ovos', 'uva')
for n in range(0,len(palavras)):
    print(f'A palavra {palavras[n]} contém: {palavras[n].count("a")} vogais a, {palavras[n].count("e")} vogais e, {palavras[n].count("i")}, vogais i, {palavras[n].count("o")} vogais o e {palavras[n].count("u")} vogais u.')
