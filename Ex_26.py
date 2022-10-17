#26: Faça um programa que leia uma frase pelo teclado # e mostre: quantas vezes aparece a letra "A", em que posição
# ela aparece a primeira vez, em que posição ela aparece a última vez.

frase = str(input("Digite aqui sua frase:")).upper().strip()

quantidade = frase.count('A')
posicao_i = frase.find('A')
posicao_f = frase.rfind('A')
print("A letra A aparece {} vezes. A primeira posição da letra A é {} e a ultima posição da letra A é {}".format(quantidade,posicao_i,posicao_f))
