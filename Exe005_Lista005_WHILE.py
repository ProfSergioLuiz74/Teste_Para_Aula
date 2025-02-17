adivinha = 50
chute = int(input("Você consegue adivinhar o número que estou pensando?\nDigite um número: "))
cont = 1
while chute != adivinha:
    if chute < adivinha:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")
    cont += 1
    chute = int(input("Tente novamente: "))
print("Parabéns! Você acertou o número em {} tentativas!".format(cont))