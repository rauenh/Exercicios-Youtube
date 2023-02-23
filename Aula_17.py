#Na lista podemos alterar seus elementos.
#Para adicionar elementos fazemos lista.append('nome do elemento') e ele vai pro final da lista
#Se vc quer inserir um elemento novo num local específico da lista, temos lista.insert(numero do index, 'item')

#del lista[3] remove pelo indice, eliminando o elemento e refazendo os indices
#lista.pop(3) remove pelo indice, geralmente remove o ultimo elemento não precisa do numero
#lista.remove('valor')

#if pizza in lanche:
    #lanche.remove('pizza')

#Criar listas através do range
#valores = list(range(4,11)) #função list pra declarar uma lista, vai contar de 4 até 10 colocando dentro de uma estrutura chamada valores. Range cria uma estrutura ordenada e crescente

#valores.sort() #ordena os valores de uma lista desorganizada
#valores.sort(reverse=True) #os valores ficam ordenados na forma inversa
#len(valores) #tamanho da lista, quantos elementos tem

#num = (2,5,9,1)
#print(num)
#num[2] = 3 #vai retornar erro

num_lista = [2,5,9,1]
print(num_lista)
num_lista[2] = 3
print(num_lista)
num_lista.append(7)
print(num_lista)
num_lista.sort()
print(num_lista)
num_lista.sort(reverse=True)
print(num_lista)
print(f'Essa lista tem {len(num_lista)} elementos.')
num_lista.insert(2,0) #na posição 2 vai inserir o zero
print(num_lista)
num_lista.pop() #remove o ultimo elemento)
print(num_lista)
num_lista.pop(2)
print(num_lista)
num_lista.insert(2,2)
print(num_lista)
num_lista.remove(2) #procura a primeira ocorrencia do numero e remove, não varre até o final, pra isso tem que fazer laço
print(num_lista)
if 4 in num_lista: #usar o contém
    num_lista.remove(4)
    print(num_lista)
else:
    print("Numero 4 não está na lista")

valores=[]
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for v in valores: #mostrar mais bonitinho
    print(f'{v}...',end='')
for c, v in enumerate(valores): #se eu quiser o indice/chaves
    print(f'Na posição {c} encontrei o valor {v}. ')
print(f'Cheguei ao fim da lista')

#for cont in range(0,5):
   # valores.append(int(input("Digite um valor:")))
#print(valores)

a = [2,3,4,7]
b = a #no momento em que vc iguala uma lsita a outra o python cria uma conexão entre as duas
c = a[:] #assim ele cria uma cópia dos valores de A em C, dado o fatiamento
b[2] = 8
print(a)
print(b)
print(c)
print(a+b)
print(b+a)