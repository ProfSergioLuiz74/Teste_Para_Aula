direcao = input('Digite a direção que deseja seguir, CIMA ou ABAIXO?(C / A): ').upper()
if direcao == 'C':
    num = int(input('Quantos numero para cima?'))
    for i in range(1,num+1):
        print(i)
elif direcao == 'A':
    num = int(input('Entre com um numero abaixo de 20: '))
    for i in range(20,num-1,-1):
        print(i)
else:
    print('Direção invalida!')

    