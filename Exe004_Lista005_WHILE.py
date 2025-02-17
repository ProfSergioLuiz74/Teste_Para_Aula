convidar = 's'
cont = 0
while convidar == 's':
    nome = input('Escreva o nome do convidado(a) para a Festa: ')
    print(nome, 'foi adicionado(a) com sucesso no convite!')
    cont += 1
    convidar = input('Deseja convidar mais alguém? (s/n): ')
print('Você convidou', cont, 'pessoas para a Festa!')