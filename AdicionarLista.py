# Inicializa a lista de produtos
produtos = []

# Loop para adicionar produtos
#while True:
    # Solicita o nome do produto ao usuário
nome_produto = input("Digite o nome do produto para adicionar (ou 'sair' para finalizar): ")
    
    # Verifica se o usuário quer sair
  #  if nome_produto.lower() == 'sair':
 #       break
    
    # Adiciona o produto à lista
produtos.append(nome_produto)
print(f"Produto '{nome_produto}' adicionado com sucesso!")
    
    # Exibe a lista atualizada de produtos
print("Lista de produtos atualizada:", produtos)

print("Programa finalizado. Lista final de produtos:", produtos)