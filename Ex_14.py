#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input("Digite aqui a temperatura em graus Celsius:"))
conversao_temp= (temperatura*9)/5 + 32

print("A temperatura em graus Celsius era de {} e em Fahrenheit é de {}".format(temperatura,conversao_temp))