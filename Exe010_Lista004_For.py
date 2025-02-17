num = int(input('Quantos amigos deseja convidar para a festa? '))
if num < 10:
    for i in range(0,num):
        nome = input("Escreva o nome do amigo: ")
        print(nome, 'está convidado para a festa!')
else:
    print('Numero muito alto!')
    