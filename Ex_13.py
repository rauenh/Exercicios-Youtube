#Desafio 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input("Digite o salário do funcionário: "))
aumento = (((15/100)*salario)/1)
salario_aumento = salario + aumento

print("Seu salario era {}, 15% do seu salário é {}. Seu novo salário com o aumento de 15% é {}".format(salario,aumento,salario_aumento))