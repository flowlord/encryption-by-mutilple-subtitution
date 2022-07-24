#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle,choice,randint
import shutil
from string import ascii_letters,digits,punctuation
import pyAesCrypt


def reinitialiser():
	"""
	Suprime vos clé de chiffrement !
	et le dossier __pycache__
	"""
	
	print('Vos clés de chiffrement vont être supprimés !')
	user = input('Etes-vous sur ? ')
		
	if user in ['y','yes','oui','o','da','Y','1']:
	
		if os.path.exists("keylib.py"):
			os.remove("keylib.py")
		shutil.rmtree('__pycache__')
		shutil.rmtree('configs/__pycache__')
		
		print('[ les clés de chiffrement ont été supprimés ]')


def gen_mdp():
	p = ""
	char = ascii_letters+digits+punctuation
	for c in range(randint(15,30)):
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

	init = open('groupes_caractere.txt','r',encoding='utf-8').readlines()
	init = "".join(init)
	init = list(init)

	for _ in range(2):
		shuffle(init)

	res = "".join(init)

	f = open('groupes_caractere.txt','w',encoding='utf-8')
	f.write(res)
	f.close()





