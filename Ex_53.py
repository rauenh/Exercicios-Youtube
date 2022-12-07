txt = str(input("Digite aqui sua frase:\n"))

y = txt.replace(' ','')
w = y.lower()
x = w[0:]
z = w[::-1]
print(y)
print(x)
print(z)

if x == z:
    print("A frase "{}" é um palindromo.".format(txt))
else:
    print("A frase {} não é um palindromo".format(txt))

