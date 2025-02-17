num = int(input("Digite um número entre 15 e 20: "))
while num<15 or num>20:
    if num<15:
        print("Muito Baixo!")
    else:
        print("Muito Alto!")    
    num = int(input("Tente novamente!"))
print("Obrigado!")