#035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
#um dos seus lados deve ser maior que o valor absoluto (modulo) da diferen;a dos outros dois lados e menor que a soma
# dos outros dois lados
import math
a = float(input("Digite a medida do primeiro lado do triângulo:\n"))
b = float(input("Digite a medida do segundo lado do triangulo:\n"))
c = float(input("Digite a medida do terceiro lado do triangulo:\n"))

if abs(b-c) < a and a < b + c:
    print("Podemos formar um triangulo de lados {}, {}, {}".format(a,b,c))
else:
    print("Não é possível formar um triângulo com essas medidas")

