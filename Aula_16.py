#tuplas são IMUTÁVEIS
lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #toda tupla é em parenteses
print(lanche)
#fatiamento
print(lanche[0:2])
print(lanche[1:])
print(lanche[1:3]) #o ultimo elemento vai ser ignorado sempre
print(lanche[-1]) #mostra o ultimo elemento
print(len(lanche)) #mostra o tamanho da variavel lanche

#Acessos a elementos da tupla
for c in lanche: #para cada comida em lanche imprime c
    print(c) #pode usar o for com range e com coleções(tuplas)
    print(f'Eu vou comer {c}')

for cont in range(0,len(lanche)):
    print(cont) #mostra as posições
    print(lanche[cont]) #mostra os itens nas posições

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Métodos em Tuplas

print(sorted(lanche)) #Ele não altera a tupla, só ordena

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #(a ordem inflencia totalmente, ele só vai juntar as tuplas)
print(c)
print(c.count(5)) #conta quantas vezes o numero aparece
print(c.index(8)) #mostra a posição que tal elemento está. Pega a primeira ocorrência do número
print(c.index(5, 1)) #o numero depois da virgula fala a posição a qual é para começarmos a procurar. DESLOCAMENTO

#Você pode ter dados de tipos diferentes dentro de uma tupla no python
#Você pode apenas apagar a tupla inteira com o comando del(tupla)

