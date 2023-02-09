#70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

print('*='*20)
print(f"{' *** CADASTRO DE PRODUTOS ***' : ^40}")
print('*='*20)
total = quantidade = barato = cont = 0
nome_barato = ''

while True:
    nome = str(input("Digite o nome do produto: "))
    preco = int(input("Digite o preço do produto:  R$ "))
    cont += 1
    menu = ' '
    while menu not in 'SN':
        menu = str(input("Deseja adicionar mais produtos a sua compra? [S/N] :")).upper().strip()[0]
    total += preco
    if preco > 1000:
        quantidade += 1
    if cont == 1 or preco < barato:
        barato = preco
        nome_barato = nome
    if menu == 'N':
        break
print('{:-^20}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra foi de R${total:.2f}. {quantidade} produtos custam mais de R$ 1000 e o produto mais barato é o {nome_barato} que custa R${barato}')

