# Ler os valores do salário e da parcela
salario = float(input("Digite o valor do salário: "))
parcela = float(input("Digite o valor da parcela: "))

# Calcular 8% do salário
limite_parcela = 0.08 * salario

# Determinar se o empréstimo pode ser concedido
if parcela < limite_parcela:
    print("Empréstimo concedido.")
else:
    print("Empréstimo não concedido.")
