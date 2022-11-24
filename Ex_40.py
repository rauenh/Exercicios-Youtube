#40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite aqui a nota 1 do aluno:\n"))
nota2= float(input("Digite aqui a nota 2 do aluno:\n"))
media = (nota1+nota2)/2

if media >= 7.0:
    print("Parabéns, você foi aprovado.Sua média é {}".format(media))
elif media <7.0 and media >= 5.0:
    print("Você está de recuperação. Sua média foi de {}".format(media))
elif media < 5.0:
    print("Você foi reprovado. Sua média foi de {}".format(media))