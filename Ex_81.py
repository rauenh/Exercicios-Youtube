#081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    menu = ' '
    numeros = lista.append(int(input("Digite um número: ")))
    while menu not in 'SN':
        menu = str(input("Você deseja adicionar mais números? [S/N]: ")).upper().strip()
    if menu == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True) #o sorte cria uma "copia temporaria" da lista na ordem desejada. Mas não dá rpafazer um n = lista.sort() etc
print(f'Os valores digitados foram {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista')
