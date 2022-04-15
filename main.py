#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE (multiple substitution encryption)

Créer le mardi 22 janvier 2019 à 01:10 

@author: FLOW LORD

twitter: https://twitter.com/flowlord_

Demo: https://youtu.be/81vH2tkX6cs
		  https://youtu.be/RRgbowrAQ0g

website: https://solarissoftwarebulares.fun/

version: MS3

supprimer le dossier __pycache__ avant de regénèrer vos clés

"""

from MSE import mse_cipher,mse_decipher,check_char,check_word,randint


example_sentences = ['meeting tonight for speak','rendez vous ce soir pour parler','hello world','on se voit ce soir','ou habitez vous',
			'que faites vous','a bientot','à la semaine prochaine','je peux te parler','on peut se voir','jusqu ici tout va bien']


print('Text chiffré:\n')
message = mse_cipher('meeting tonight for speak')
print(message,'\n\n')

print('Texte déchiffré:\n')
print(mse_decipher(message))

