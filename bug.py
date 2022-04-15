from MSE import mse_cipher,mse_decipher,check_char

n,c = 0,100

for e in range(c):
	m = mse_cipher("hello world")
	if check_char(m) is False:
		pass
	else:
		n = n+1


	if n == 0:
		print("Aucun bug de déchiffrement détecté")


print(f"{n}/{c} des messages chiffrées son illisible")



