#51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input("Digite aqui o primeiro termo da PA:\n"))
r = int(input("Digite aqui a razão da PA:\n"))
n = int(input("Digite aqui a posição do termo que queremos descobrir:\n"))

for c in range (1,n+1):
    an = a1 + (c -1)*r
    print(an)
print("O {} termo da PA de razão {} e primeiro termo {} é {}".format(n,r,a1,an))