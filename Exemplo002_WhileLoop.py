vendas = [941,852,783,714,697,686,670,631,453,386,371,294,269,259,218,208,163,125,87,47,7]
vendedores = ['Maria','João','José','Ana','Carlos','Pedro','Paulo','Lucas','Marta','Joaquim','Júlia','Ricardo','Fernando','Mariana','Sandra','Lúcia','Rafael','Gustavo','Eduardo','Roberto','Ricardo']
meta = 50
i = 0
while vendas[i] > meta:
    print('{} bateu a meta. Vendas: {}'.format(vendedores[i],vendas[i]))

    