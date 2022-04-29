#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle
import shutil
from random import choice

def gen_many_keylib(x,keyNumber):
	
	print('[ génération des clés de chiffrement ... ]\n')

	d = 'keylib lib'
	os.makedirs(d,exist_ok = True)

	for x in range(1,x+1):
		name = d+"/keylib_" + str(x)+".py"

		file = open(name,'w',encoding='utf-8')
		    
		file.write('# coding: utf-8\n')
		file.write('from random import choice\n')
		    
		for number in range(1,keyNumber+1):
			file.write(f'KEY{number} = {keygen(nbr_letter_sub)}\n')
			    
		file.write(f'listkey = {gen_listkey(keyNumber)}\n')

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
	if os.path.exists("keylib.py"):
		os.remove("keylib.py")
	else:
		pass

	try:
		shutil.rmtree('__pycache__')
	except FileNotFoundError:
		pass


def mixer_string(string):
	"""
	Mélange les caractères
	Provoque des bugs si on utilise la fonction shuffle
	dû à la conversion de la chaine de caractère vers une liste
	"""
	n = ''
	d = string
	while len(string) != len(n):
		c = choice(d)
		n = n +c
		d = d.replace(c,"")

	return n


def mixer():
	"""
	exemple:
		AAAZZZ ---> | mixer(2) | ---> ZAAZAZ
	"""
	reinitialiser()

	init = open('initpat.txt','r',encoding='utf-8').read()

	for _ in range(2):
		init = mixer_string(init)

	f = open('initpat.txt','w',encoding='utf-8')
	f.write(init)
	f.close()


