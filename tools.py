#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle,choice,randint
import shutil
from string import ascii_letters,digits,punctuation
import pyAesCrypt


def gen_many_keylib(x,keyNumber):
	
	print('[ Generating and writing keylib ... ]\n')

	d = 'keylib lib'
	os.makedirs(d,exist_ok = True)

	for x in range(1,x+1):
		name = d+"/keylib_" + str(x)+".py"

		file = open(name,'w',encoding='utf-8')
		    
		file.write('# coding: utf-8\n')
		file.write('from random import choice\n\n')
		    
		for number in range(1,keyNumber+1):
			file.write(f'KEY{number} = {keygen(nbr_letter_sub)}\n')
			    
		file.write(f'listkey = {gen_listkey(keyNumber)}\n\n')

		file.write('def getRandomKey():\n')
		file.write('\treturn choice(listkey)')
		
		file.close()

		print(f'{x} keylib generated')


def reinitialiser():
	"""
	Suprime vos clé de chiffrement !
	et le dossier __pycache__
	pratique lorsque vous modifiez le code source
	"""
	print('Vos clés de chiffrement vont être supprimés !')
	user = input('Etes-vous sur ? ')
		
	if user in ['y','yes','oui','o','da','Y','1']:
	
		if os.path.exists("keylib.py"):
			os.remove("keylib.py")
		shutil.rmtree('__pycache__')
		
		print('[ les clés chiffrement ont été supprimés ]')


def gen_mdp():
	p = ""
	char = ascii_letters+digits+punctuation
	
	for c in range(randint(10,15)):
		p = p + choice(char)
	
	return p


def encrypt_keylib():
	"""
	pour chiffrer vos clés de chiffrement.

	"""
	if os.path.exists("keylib.py"):
		password = gen_mdp()
		print('mot de passe: ',password)
		pyAesCrypt.encryptFile("keylib.py", "keylib.aes", password)
		
	else:
		pass


def decrypt_keylib(password):
	"""
	pour déchiffrer vos clés de chiffrement.

	"""
	if os.path.exists("keylib.aes"):
		pyAesCrypt.decryptFile("keylib.aes", "keylib.py", password)
	else:
		pass


def mixer():
	"""
	Mélange l'ordre des caractères
	example:
		AAAZZZ ---> | mixer(2) | ---> ZAAZAZ
	"""
	reinitialiser()

	init = open('initpat.txt','r',encoding='utf-8').readlines()
	init = "".join(init)
	init = list(init)

	for _ in range(2):
		shuffle(init)

	res = "".join(init)

	f = open('initpat.txt','w',encoding='utf-8')
	f.write(res)
	f.close()






