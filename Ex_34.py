#034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# -Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# -Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input("Digite aqui seu salario em reais:\n"))

if salario > 1250.00:
    aumento = (salario*10)/100
    sal_au = salario + aumento
    print("Seu salario com aumento é de {}".format(sal_au))
else:
    if salario <= 1250.00:
        aumento2 = (salario*15)/100
        sal_au2 = salario + aumento2
        print("Seu salario com aumento é de {}".format(sal_au2))