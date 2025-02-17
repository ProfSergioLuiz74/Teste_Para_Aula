# Inicializa as listas para armazenar as tarefas e seus status
tarefas = []
status_tarefas = []

# Solicita ao usuário para inserir o número de tarefas
num_tarefas = int(input("Quantas tarefas você deseja inserir? "))

# Loop para inserir as tarefas e seus status
for i in range(num_tarefas):
    tarefa = input(f"Digite o nome da tarefa {i + 1}: ")
    status = input(f"A tarefa '{tarefa}' está concluída? (sim/s/não/n): ").lower()
    tarefas.append(tarefa)
    status_tarefas.append(status)

# Contadores para tarefas concluídas e não concluídas
concluidas = 0
nao_concluidas = 0

# Loop para contar as tarefas concluídas e não concluídas
for status in status_tarefas:
    if status in ['sim', 's']:
        concluidas += 1
    elif status in ['não', 'n']:
        nao_concluidas += 1

# Exibe o resultado
print(f"\nTotal de tarefas: {num_tarefas}")
print(f"Tarefas concluídas: {concluidas}")
print(f"Tarefas não concluídas: {nao_concluidas}")

