a1 = int(input("Digite aqui o primeiro termo da PA:\n"))
r = int(input("Digite aqui a razão da PA:\n"))
n = a1
c = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(n), end='')
        n = n + r
        c +=1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais?"))
print('FIM')
print("PA finalizada com {} termos.".format(total))
