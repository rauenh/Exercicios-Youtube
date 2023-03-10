#083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite aqui sua expressão matemática: ")).split()
print(expressao)
quantidade = 0
for elementos in expressao:
    print(elementos)
    quantidade = elementos.count('(') + elementos.count(')')
    if quantidade%2 == 0:
        print("A expressão é válida")
    else:
        print("A quantidade de parênteses não está correta")

print(quantidade)
