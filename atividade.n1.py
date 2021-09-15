from random import randint

venceu = 0
jogadas = 0 
sala = 1



while venceu == 0:
	while jogadas< 7:
		print("Voce esta na sala:",sala)
		print("jogadas restantes:",7-jogadas)
		print("Escolha seu caminho:")
		print("[1] - Caminho vermelho")
		print("[2] - Caminho preto")
		escolha = int(input(""))
		break;
	while escolha == 1:
		sala +=1
		jogadas +=1
		break;
	while escolha == 2:
		sala+=2
		jogadas+=1
		break;
        if sala == 9:
		print("Casa 9 você venceu!!")
		venceu == 1	
		break;
	elif jogadas >=7:
		print("Você perdeu :( ")
		break;
	while sala == 6:
		print("Voce esta na sala:",sala)
		print("jogadas restantes:",7-jogadas)
		print("Escolha seu caminho:")
		print("[2] - Caminho preto")
		escolha = int(input(""))
		while escolha == 1:
			print("")
			print("caminho indisponível!")
			print("")
			print("Escolha seu caminho:")
			print("[2] - Caminho preto")
			escolha = int(input(""))
		break;
	while escolha == 2 and sala == 6:
		sala +=2
		jogadas +=1
		break;
while sala == 8:
		print("Voce esta na sala:",sala)
		print("jogadas restantes:",7-jogadas)
		print("Escolha seu caminho:")
		print("[1] - Caminho vermelho")
		print("[2] - Caminho preto")
		escolha = int(input(""))
		break;
	while escolha == 1 and sala == 8:
		sala +=1
		jogadas +=1
		break;
	while escolha == 2 and sala == 8:
		jogadas+=1
		sala= randint(1,5)
		break;
