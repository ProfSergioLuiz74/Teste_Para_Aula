def handle_A():
	print("Errado! Tente novamente!")

def handle_B():
	print("Absolutamente certo! Trillium é um tipo de flor!")

def handle_C():
	print("Errado! Tente novamente!")

print("\n" * 100)
# clear the screen
print("            JOGO DE ADIVINHAÇÃO MUITO DESAFIADOR")
print("========================================================")
# 5
# GRUPO PYTHON – UNESP – ILHA SOLTEIRA
# STEVEN FERG
# PENSANDO EM TKINTER
print("Pressione a letra da sua resposta e, em seguida, a tecla ENTER.")
print()
print("    A.  Animal")
print("    B.  Vegetable")
print("    C.  Mineral")
print()
print("    X.  Saída deste programa")
print()
print("========================================================")
print("Que tipo de coisa é 'Trillium'?")

# Questão 4: O Event Loop. Loop eterno, esperando que algo aconteça.
while 1:
	# Observamos o próximo evento
	answer = input().upper()
	# -------------------------------------------------------------
	# Questão 3: Associamos os eventos de teclado que nos interessam
	# com seus event handlers. Uma forma simples de binding.
	# -------------------------------------------------------------
	if answer == "A":
		handle_A()
	elif answer == "B":
		handle_B()
	elif answer == "C":
		handle_C()
	elif answer == "X":
		# clear the screen and exit the event loop
		print("\n" * 100)
		break
	# Perceba que quaisquer outros eventos não interessam, por isso são
	# ignorados.