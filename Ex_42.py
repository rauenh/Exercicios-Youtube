#42: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois lados iguais, um diferente - ESCALENO: todos os lados diferentes
#ABS retorna valor absoluto do numero)

a = float(input("Digite a medida do primeiro lado do triângulo:\n"))
b = float(input("Digite a medida do segundo lado do triangulo:\n"))
c = float(input("Digite a medida do terceiro lado do triangulo:\n"))

if abs(b-c) < a and a < b + c:
    print("Podemos formar um triangulo de lados {}, {}, {}".format(a,b,c))

    if a == b == c:
        print("Você formará um triângulo EQUILÁTERO")
    elif a==b or a==c or b==c:
        print("Você formará um triangulo ISOSCELES")
    else:
        print("Você formará um triangulo ESCALENO")
else:
    print("Não é possível formar um triângulo com essas medidas")