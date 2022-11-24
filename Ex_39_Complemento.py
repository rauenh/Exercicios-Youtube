from datetime import date
atual = date.today().year
nascimento = int(input("Digite aqui seu ano de nascimento:\n"))
alistamento = nascimento + 18

if alistamento < atual:
    tempo = atual - alistamento
    print("Ja se passaram {} anos para o alistamento militar obrigatório. Você deveria ter se alistado em {}".format(tempo,alistamento))
elif alistamento > atual:
    tempo = alistamento - atual
    print("Falta {} anos do alistamento militar obrigatório. Você deverá se alistar em {}".format(tempo, alistamento))
elif alistamento == atual:
    print("Você deve fazer o alistamento militar obrigaório esse ano de {}".format(alistamento))