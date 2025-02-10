#TRANSFORMA APENAS A PRIMEIRA LETRA DE UMA STRING EM MAIUSCULA
nome = "sergio"
print(nome.capitalize(),"\n")

#TRANSFORMA TODAS AS LETRAS EM MINUSCULA
nome = "SERGIO"
print(nome.casefold(),"\n")

#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING.
nome = "SergioLuiz@gmail.com"
print(nome.count('i'),"\n")

#RETORNA true (verdadeiro) OU false (falso) PARA UM TESTE se A STRING TERMINA COM UMA STRING ESPECIFICA.
nome = "SergioLuiz@gmail.com"
print(nome.endswith('gmail.com'),"\n")


#ENCONTRA A POSIÇÃO DO TERMO PROCURADO.LEMBRE-SE COMEÇA DO zero
nome = "SergioLuiz@gmail.com"
print(nome.find('@'),"\n")


#VERIFICA SE O TEXTO É todo FEITO COM LETRAS.
nome = "Sergio"
print(nome.isalpha(),"\n")


#VERIFICA SE O TEXTO É FEITO COM numeros.
nome = "123"
print(nome.isnumeric(),"\n")


#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO.
nome = "Sergio"
print(nome.replace('o','u'),"\n")


#SEPARA O TEXTO string BASEADO EM ALGUM CARACTERE INDICADO.
nome = "Sergio @ Paula Fernandes"
print(nome.split('@'),"\n")


#COLOCAR TODAS AS LETRAS INICIAIS EM maiuscula.
nome = "sergio luiz da silveira"
print(nome.title(),"\n")

#RETIRA OS CARACTERES INDESEJADOS, COMO POR EXEMPLO espaços QUE NAO AGRAGAM VALOR.
nome = "  sergio luiz da silveira  "
print(nome.strip(),"\n")

#RETORNA true OU false PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO.
nome = "sergio 1980"
print(nome.startswith("ser"),"\n")
print(nome.startswith("Ser"),"\n")


#COLOCAR TODAS AS LETRAS EM maiuscula.
nome = "sergio luiz da silveira"
print(nome.upper(),"\n")