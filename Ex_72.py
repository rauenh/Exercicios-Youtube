#072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    opcao = int(input("Digite um número de 0 a 20:"))
    if 0 <= opcao <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {contagem_extenso[opcao]}')
#for cont in range(0,len(contagem_extenso) + 1):
   # print(cont)
   # print(contagem_extenso[cont])

if opcao < 20:
    print(f'Você digitou o número: {contagem_extenso[opcao]}')
elif opcao == 20:
    print(f'Você digitou o número: {contagem_extenso[-1]}')
