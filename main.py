#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE (multiple substitution encryption)

Créer le mardi 22 janvier 2019 à 01:10 

@author: Flow Lord

twitter: https://twitter.com/flowlord_

démo: https://youtu.be/81vH2tkX6cs
		  https://youtu.be/RRgbowrAQ0g

site web: https://solarissoftwarebulares.fun/

version: MS3

supprimer le dossier __pycache__ avant de regénèrer vos clés

"""

from MSE import mse_cipher,mse_decipher

example_phrase = ['meeting tonight for speak','rendez vous ce soir pour parler','hello world','on se voit ce soir','ou habitez vous',
			'que faites vous','a bientot','à la semaine prochaine','je peux te parler','on peut se voir','jusqu ici tout va bien']

def chiffrer_plusieurs_messages(liste):
	for message in liste:
		print(mse_cipher(message),'\n')


def déchiffrer_plusieurs_messages(liste):
	for message in liste:
		print(mse_decipher(message),'\n')


def demo():
	print('Text chiffré:\n')
	message = mse_cipher('meeting tonight for speak')
	print(message,'\n\n')

	print('Texte déchiffré:\n')
	print(mse_decipher(message))

demo()


