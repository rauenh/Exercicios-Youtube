#62: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
a1 = int(input("Digite aqui o primeiro termo da PA:\n"))
r = int(input("Digite aqui a razão da PA:\n"))
n = a1
c = 1
print("A calcular os 10 termos da PA começando em {} e de razão {}. ".format(a1,r))
while c <= 10:
    print('{} -> '.format(n), end='')
    n = n + r
    c +=1
print("FIM. \nEsses são os 10 termos da PA.")
menu= int(input("Deseja calcular mais termos? \n Digite 1 para SIM ou 2 para NÃO.\n Digite sua opção: "))
if menu == 1:
    termosextra = int(input("Quantos termos a mais você deseja calcular?"))
    novostermos = 10 + termosextra
    c1 = 10
    while c1 < novostermos:
        print('{} -> '.format(n), end='')
        n = n + r
        c1+=1
    print("FIM! \nO {} termo da PA de razão {} e primeiro termo {} é {}".format(novostermos,r,a1,(n-r)))
else:
    print("Programa finalizado")


