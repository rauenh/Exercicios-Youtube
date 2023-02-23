#076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

mercadinho = ('Doce de leite', '1,99', 'Manteiga', '3,99', 'Macarrao', '3,99', 'Duzia Ovos', '8,99' )
#print(mercadinho)
preco = tuple(mercadinho[i] for i in range (len(mercadinho)) if i%2 != 0)
print(preco)
produto = tuple(mercadinho[i] for i in range (len(mercadinho)) if i%2 ==0)
print(produto)

#for cont in range(0,len(mercadinho), 2):
    #print("\n", mercadinho[cont], end=' ') #mostra os itens nas posições
#for cont in range (1,len(mercadinho),2):
    #print("\n", mercadinho[cont], end='')

c=0
print(f"{ 'Produto' :^20} | { 'Preço' :^20} ")
while c < len(produto):
#for c in range(0,len(produto)):
    print(f"{produto[c] :.<20} R${preco[c] :>10} ")
    c += 1


