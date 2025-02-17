nome = input("Escreva seu nome: ")
num = int(input('Digite um numero: '))
if num < 10:
    for i in range(0,num):
        print(nome)
else:
    for i in range(0,3):
        print('Numero muito alto!')

        