total = 0
for i in range(0, 5):
    num = int(input('Digite um numero: '))
    resultado = input('Você quer incluir esse um numero? (S ou N)').upper()
    if resultado == 'S':
        total = total +num
print('A soma dos numeros é: ', total)
print('Fim do programa')    

