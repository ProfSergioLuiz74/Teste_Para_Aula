# OPERAÇAO ROTINEIRA: Cálculo de média aritmética
nota1 = input("Digite a 1a nota: ")
nota2 = input("Digite a 2a nota: ")
media = (float(nota1) + float(nota2)) / 2
print("A média é: ", media)

#CRIANDO UMA FUNÇÃO: Cálculo de média aritmética:
def calcula_media(nota3, nota4):
    nota3 = input("Digite a primeira nota: ")
    nota4 = input("Digite a segunda nota: ")
    media = (float(nota3) + float(nota4)) / 2
    return print('A média das notas é: {}.'.format(media))

# CHAMANDO A FUNÇAO QUE ACABAMOS DE CRIAR
calcula_media(1,1)
print('Fim programa')