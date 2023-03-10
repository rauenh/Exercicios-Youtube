#083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite aqui sua expressão matemática: ")).split()
print(expressao)
print(expressao.count('('))
print(expressao.count(')'))
quantidade = 0
for elementos in expressao:
    print(elementos)
    quantidade = elementos.count('(') + elementos.count(')')
    if quantidade%2 == 0:
        if elementos.index(')') < elementos.index(')', 1):
            print("O parenteses não está na ordem correta")
        elif elementos.index('(') > elementos.index('(', 1):
            print("O parenteses não está na ordem correta")
        elif elementos.index('(') > elementos.index(')'):
            print("O parenteses está fora da ordem")
        elif elementos.count('(') >= 2 and elementos.count(')') == 0:
            print("Parênteses do tipo '(' em excesso e fora da ordem")
        elif elementos.count(')') >= 2 and elementos.count('(') == 0:
            print("Parênteses do tipo ')' em excesso e fora da ordem")
        else:
            print("A quantidade de parenteses está na ordem correta")
    else:
        print("A quantidade de parênteses não está correta")

print(quantidade)
