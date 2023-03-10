#082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

lista = []
lista_impar = []
lista_par = []
while True:
    menu = ' ' #Para o menu sempre iterar novamente sua variável tem que ficar dentro
    numeros = lista.append(int(input("Digite um número: ")))
    while menu not in 'SN':
        menu = str(input("Você deseja adicionar mais números? [S/N]: ")).upper().strip()
    if menu == 'N':
        break
for elementos in lista: #uma outra forma de fazer é usando um for i, v in enumerate(lista): if v%2 ==0, pares.append(v) elif v%2 == 1: impares.append(v)
    if elementos%2 == 0:
        lista_par.append(elementos)
    if elementos%2 != 0:
        lista_impar.append(elementos)
print(f'Os números digitados foram {lista}.)
print(f' Os números ímpares são: {lista_impar})
print(f'Os números pares são: {lista_par})
