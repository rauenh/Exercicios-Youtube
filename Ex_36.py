#36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

valor_casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o valor do seu salario?"))
anos = int(input("Em quantos anos vc deseja pagar a casa?"))

parcela_valor = valor_casa/(anos*12)
parcela_quant = anos*12
verificar_sal = (30*salario)/100

if parcela_valor <= verificar_sal:
    print("Emprestimo aprovado. Vc pagara {:.2f} reais em {} parcelas, totalizando {} reais em {} anos".format(parcela_valor,parcela_quant,valor_casa,anos))
else:
    print("Seu emprestimo não foi aprovado. A parcela é de {:.2f} e excede os 30% do seu salario que é {}".format(parcela_valor,verificar_sal))

