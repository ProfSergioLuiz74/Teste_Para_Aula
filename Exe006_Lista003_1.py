# Solicita o nome do município, a quantidade de eleitores e a quantidade de votos do candidato mais votado
nome_municipio = input("Digite o nome do município: ")
quantidade_eleitores = int(input("Digite a quantidade de eleitores: "))
votos_mais_votado = int(input("Digite a quantidade de votos do candidato mais votado: "))

# Verifica se haverá segundo turno
if quantidade_eleitores >= 200000 and votos_mais_votado <= (quantidade_eleitores / 2):
    print(f"No município de {nome_municipio}, haverá segundo turno.")
else:
    print(f"No município de {nome_municipio}, não haverá segundo turno.")