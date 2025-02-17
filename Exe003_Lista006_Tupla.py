nome1 = input('Digite o nome do convidado(a) para a festa: ')
nome2 = input('Digite o nome do convidado(a) para a festa: ')
nome3 = input('Digite o nome do convidado(a) para a festa: ')
convidados = [nome1, nome2, nome3]
mais_convidados = input('Deseja convidar mais alguém? (s/n) ')
while mais_convidados == 's':
    novo_nome = convidados.append(input('Digite o nome do convidado(a) para a festa: '))
    mais_convidados = input('Deseja convidar mais alguém? (s/n) ')
print('Você convidou',len(convidados),'pessoas para a festa')
print(convidados)
selecione = input('Digite um nome de convidado(a): ')
print(selecione,'este(a) convidado(a) está na posição: ',convidados.index(selecione),'da lista')
continua_convidado = input('Deseja manter o convidado(a)? (s/n) ')
if continua_convidado == 'n':
    convidados.remove(selecione)
print(convidados)
print('Fim do programa')

