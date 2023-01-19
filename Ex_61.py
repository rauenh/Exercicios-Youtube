#61: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input("Digite aqui o primeiro termo da PA:\n"))
r = int(input("Digite aqui a razão da PA:\n"))
n = int(input("Digite aqui a posição do termo que queremos descobrir:\n"))
c = 0

while c != n:
    an = a1 + (n-1)*r
    print(an)
    c +=1

print("O {}º termo da PA de razão {} e de primeiro termo {} vale: {}".format(n, r, a1, an))
