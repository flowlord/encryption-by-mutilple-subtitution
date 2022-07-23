#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

	███╗   ███╗  ██████╗ ███████╗
	████╗ ████║ ██╔════╝ ██╔════╝
	██╔████╔██║ ╚█████╗  █████╗
	██║╚██╔╝██║  ╚═══██╗ ██╔══╝
	██║ ╚═╝ ██║ ██████╔╝ ███████╗
	╚═╝     ╚═╝ ╚═════╝  ╚══════╝
	
	MSE (multiple substitution encryption)

	Créer le mardi 22 janvier 2019 à 01:10 

	@author: Motion Kerling

	twitter: https://twitter.com/motionkerling

	version name: CRC V
	
"""

__doc__ = """
Uasage:
	
	1) Chiffrer et déchiffrer un message
		-------------------------------------------->
		main.py c "message"
		main.py d (le message est automatiquement copier)


	2) Pour chiffrer les clés
		---------------------->
		main.py cry
		main.py des PASSWORD


	3) Supprimer les clés
		---------------------->
		main.py R

		
		
	4) Mélanger les caractères spéciaux
		---------------------->
		main.py M
		
"""


from pyperclip import paste
from pyperclip import copy as copier_text
from tools import encrypt_keylib,decrypt_keylib,reinitialiser,mixer
import sys
from random import choice,randint
from configs.parametre import*
from bloc_a import complexi,decomplex
from bloc_b import cipher,decipher
from bloc_c import chaos,dechaos


example_phrases = ['ceci est une longue phrase un peut chiante','meeting tonight for speak','rendez vous ce soir pour parler','hello world','on se voit ce soir','ou habitez vous','que faites vous','a bientot','a la semaine prochaine','je peux te parler','on peut se voir','jusqu ici tout va bien','mec tfk quoi la','alors la je fait expres de mettre une tres longue phrase pour des test','hallo zusammen heute']


def demo():
	print('---------- * DEMO * ----------')
	print('Text chiffré:\n')
	message = mse_cipher(choice(example_phrases))
	print(message,'\n\n')

	print('Texte déchiffré:\n')
	print(mse_decipher(message))


def mse_cipher(msg):
	"""
	|A| --> |B| --> |C|
	"""
	a  = complexi(msg)
	b = cipher(a)
	c = chaos(b,randint(mini,maxi))
	
	copier_text(c)
	return c


def mse_decipher(msg):
	"""
	|C| --> |B| --> |A|
	"""
	c = dechaos(msg)
	b = decipher(c)
	a = decomplex(b)
	
	return a


def main():

	cip = ['cipher','c','C','cip']
	dec = ['decipher','d','D','dec']
	cryp = ['cryp','cr','cry']
	des = ['des','de','decr']
	mxr = ['M','m','mixer','mix','mxr']
	reset = ['r','R','reset','delete','del']
	h = ['H','h','Help me','aide moi','A','a']
	
	_all_ = cip+dec+cryp+des+reset+mxr+h
	
	if sys.argv[1] not in _all_:
		if sys.argv[1] == "demo":
			demo()
		else:
			print('commande invalide')
		
	elif sys.argv[1] in cip:
		print(mse_cipher(sys.argv[2]))
		
	elif sys.argv[1] in dec:
		print(mse_decipher(paste()))
	
	elif sys.argv[1] in cryp:
		encrypt_keylib()
		
	elif sys.argv[1] in des:
		decrypt_keylib(paste())
	
	elif sys.argv[1] in reset:
		reinitialiser()
	
	elif sys.argv[1] in mxr:
		mixer()
	
	elif sys.argv[1] in h:
		print(__doc__)


main()


