#61: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input("Digite aqui o primeiro termo da PA:\n"))
r = int(input("Digite aqui a razão da PA:\n"))
n = a1
c = 1

while c <= 10:
    print('{} -> '.format(n), end='')
    n = n + r
    c +=1
print("FIM.Esses são os 10 termos da PA.")

