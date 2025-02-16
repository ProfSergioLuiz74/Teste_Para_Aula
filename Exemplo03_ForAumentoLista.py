produtos = ['coca cola', 'pepsi', 'guarana','sprite','fanta','Agua da Serra']
producao = [15000,12000,13000,5000,250,3500]

tamanho = len(produtos)

for i in range(tamanho): # PERMITE AUMENTAR A LISTA
    print('A produção de {} é de {}'.format(produtos[i],producao[i]))  