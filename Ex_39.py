#39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
#se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nascimento = int(input("Digite aqui seu ano de nascimento:\n"))
data = int(input("Digite o ano que estamos:\n"))
alistamento = nascimento + 18

if alistamento < data:
    tempo = data - alistamento
    print("Ja se passaram {} anos para o alistamento militar obrigatório".format(tempo))
elif alistamento > data:
    tempo = alistamento - data
    print("Falta {} anos do alistamento militar obrigatório".format(tempo))
elif alistamento == data:
    print("Você deve fazer o alistamento militar obrigaório esse ano")