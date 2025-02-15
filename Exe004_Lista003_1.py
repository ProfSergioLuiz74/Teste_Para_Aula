# Programa para verificar se a pessoa será aceita para o serviço militar em Sanailândia

# Leitura dos dados de entrada: nome, idade e sexo
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
sexo = input("Digite o sexo da pessoa (f/F para feminino, m/M para masculino): ")

# Verificação das condições de aceitação
if sexo.lower() == 'f':
    if 21 <= idade <= 34:
        print(f"{nome} será aceita para o serviço militar.")
    else:
        print(f"{nome} não será aceita para o serviço militar devido à idade.")
elif sexo.lower() == 'm':
    if 18 <= idade <= 39:
        print(f"{nome} será aceito para o serviço militar.")
    else:
        print(f"{nome} não será aceito para o serviço militar devido à idade.")
else:
    print("Sexo inválido. Por favor, insira 'f' ou 'F' para feminino e 'm' ou 'M' para masculino.")