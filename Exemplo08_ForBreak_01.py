pessoas_presentes = ['John Snow','Jesse Pinkman','Aria Stark','Tyrion Lannister']
# QUERO SABER SE UMA PESSOA ESPECIFICA ESTÁ PRESENTE.
chamada = 'Aria Stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} está presente.'.format(chamada))
        break
    else:
        print('Só um print para mostrar que o for passou por essa pessoa:'+str(pessoa))