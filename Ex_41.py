#41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade: - Até 9 anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos: JÚNIOR - Até 25 anos: SÊNIOR - Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
nascimento = int(input("Digite aqui o ano do seu nascimento:\n"))
compara = atual - nascimento
if compara <= 9:
    print("Sua categoria é a MIRIM, sua idade é de {}".format(compara))
elif compara > 9 and compara <=14:
    print("Sua categoria é INFANTIL, sua idade é de {}".format(compara))
elif compara >14 and compara <=19:
    print("Sua categoria é JUNIOR, sua idade é de {}".format(compara))
elif compara > 19 and compara <=25:
    print("Sua categoria é SENIOR, sua idade é de {}".format(compara))
else:
    print("Sua categoria é MASTER, sua idade é de {}".format(compara))