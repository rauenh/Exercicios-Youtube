#Algoritmo de Ordenação
#Primeiro passo: criar lista
lista = []
#recebendo os 5 números
for c in range (0,5):
    n = int(input("Digite um número: ")) #foi criada uma variável pois se usar apenas o lista.append(n) o número vai para o final da lista direto. Precisamos ter uma forma de colocá-lo na lista de maneira organizada.
    #Segundo passo: descobrir onde vai adicionar. Tem 3 possibilidades: Início da lista, meio da lista e último da lista. Se for adicionar na primeira posição da lista, será apenas append no indice 0.
    #Para saber o ultimo valor n > lista[len(lista-1)] ou n > lista[-1]
    #Se o número for maior do que o ultimo valor, faz um append também
    #Temos duas formas de fazer o primeiro/ultimo posição. Com if e elif, ou if com or
    if c == 0 or n > lista[-1]: #O numero sempre será adicionado na posição 0 e ultima posição se:
        lista.append(n)
        print('Adicionando ao final da lista')
    else: #verificar, começa varrendo o vetor inteiro. Vai da posição 0 até a ultima posição. Pra cada posição ele verifica se o número a ser inserido é menor ou igual ao número que está na posição (lista[pos]). Dai ao invés de usar append, usa-se o lista.insert pois vc consegue inserir na posição desejada.
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')#na posição X insere o numero n em questão
                break
            pos += 1
print('=*'*30)
print(f'os valores digitados foram {lista}')

#então a ideia do algoritmo de ordenação numa lista é