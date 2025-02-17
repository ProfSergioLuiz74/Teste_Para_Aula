num1 = int(input("Digite o primeiro número: "))
total = num1
resposta = 's'
while resposta == 's':
    num2 = int(input("Digite o próximo número: "))
    total = total + num2
    resposta = input("Deseja digitar mais um número? (s/n): ")
print("O total é: ", total)
print("Programa encerrado.")