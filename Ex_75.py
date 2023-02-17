#075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

tupla = (int(input("Digite um valor:")), int(input("Digite um valor:")), int(input("Digite um valor:")), int(input("Digite um valor:")))
print(tupla)

print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'A posição do primeiro valor 3 foi a posição {tupla.index(3)} da tupla.')
else:
    print("O numro 3 não está na tupla")
for c in tupla: #c é o elemento da tupla
    if (c%2 ==0):
        print(f"Os numeros pares são {c}")

