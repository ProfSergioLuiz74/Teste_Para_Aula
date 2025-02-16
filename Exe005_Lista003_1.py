# Solicita o preço de custo do produto ao usuário
preco_custo = float(input("Digite o preço de custo do produto: "))

# Verifica a margem bruta com base no preço de custo
if preco_custo <= 100.00:
    margem_bruta = 0.45
else:
    margem_bruta = 0.35

# Calcula o preço de venda
preco_venda = preco_custo * (1 + margem_bruta)

# Exibe o preço de venda com duas casas decimais
print(f"O preço de venda do produto é: R$ {preco_venda:.2f}")