# Lista de convidados
convidados = ["Albert Einstein", "Isaac Newton", "Marie Curie"]

# Mensagens de convite
for convidado in convidados:
    print(f"Olá {convidado}, você está convidado para um jantar.")

# Convidado que não poderá comparecer
print(f"\nInfelizmente, {convidados[1]} não poderá comparecer ao jantar.")

# Substituindo o convidado
convidados[1] = "Nikola Tesla"

# Novo conjunto de mensagens de convite
for convidado in convidados:
    print(f"Olá {convidado}, você está convidado para um jantar.")

# Informando sobre a mesa maior
print("\nEncontrei uma mesa de jantar maior, então vou convidar mais pessoas.")

# Adicionando novos convidados
convidados.insert(0, "Galileo Galilei")
convidados.insert(2, "Ada Lovelace")
convidados.append("Charles Darwin")

# Novo conjunto de mensagens de convite
for convidado in convidados:
    print(f"Olá {convidado}, você está convidado para um jantar.")

# Informando sobre a redução da lista de convidados
print("\nInfelizmente, só posso convidar duas pessoas para o jantar.")

# Removendo convidados até restarem apenas dois
while len(convidados) > 2:
    removido = convidados.pop()
    print(f"Desculpe, {removido}, mas não posso convidá-lo para o jantar.")

# Mensagens para os dois convidados restantes
for convidado in convidados:
    print(f"Olá {convidado}, você ainda está convidado para o jantar.")

# Removendo os dois últimos convidados
del convidados[0]
del convidados[0]

# Garantindo que a lista está vazia
print("\nLista de convidados final:", convidados)