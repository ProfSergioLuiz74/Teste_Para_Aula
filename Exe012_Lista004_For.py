# Inicializa a lista para armazenar os horários disponíveis
horarios_disponiveis = []

# Solicita à dona do salão para inserir o número de horários disponíveis
num_horarios = int(input("Quantos horários disponíveis você deseja inserir? "))

# Loop para inserir os horários disponíveis
for i in range(num_horarios):
    horario = input(f"Digite o horário disponível {i + 1} (formato HH:MM): ")
    horarios_disponiveis.append(horario)

# Número máximo de tentativas de agendamento
max_tentativas = num_horarios

# Loop para agendar horários
for tentativa in range(max_tentativas):
    # Verifica se ainda há horários disponíveis
    if not horarios_disponiveis:
        print("\nNão há mais horários disponíveis para agendamento.")
        break
    
    # Exibe os horários disponíveis
    print("\nHorários disponíveis:")
    for horario in horarios_disponiveis:
        print(horario)
    
    # Solicita à cliente para escolher um horário
    novo_horario = input("\nDigite o horário que você deseja agendar (formato HH:MM): ")

    # Verifica se o novo horário está disponível e agenda
    if novo_horario in horarios_disponiveis:
        horarios_disponiveis.remove(novo_horario)
        print(f"\nHorário {novo_horario} foi agendado com sucesso.")
    else:
        print(f"\nHorário {novo_horario} não está disponível.")

    # Pergunta se deseja agendar mais um horário
    if tentativa < max_tentativas - 1:
        continuar = input("\nDeseja agendar mais um horário? (sim/s/não/n): ").lower()
        if continuar not in ['sim', 's']:
            break

# Exibe os horários restantes disponíveis
if horarios_disponiveis:
    print("\nHorários restantes disponíveis:")
    for horario in horarios_disponiveis:
        print(horario)
else:
    print("\nTodos os horários foram agendados.")

    