faturamento = input('Qual foi o faturamento da loja nesse mês? ')
custo = input('Qual foi o custo da loja nesse mês? ')
if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print('O lucro da loja foi de {} reais'.format(lucro))
else:
    print('Algum valor não foi fornecido')


