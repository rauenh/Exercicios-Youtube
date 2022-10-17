usuario = input("Digite alguma coisa aqui:")

if usuario.isalnum():
    print("é alfa numerico")
if usuario.isalpha():
    print("é alfabético")
if usuario.isnumeric():
    print("é numérico")