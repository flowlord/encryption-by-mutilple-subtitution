#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

I) Je chsoit un groupe de caractère que je veut subtituer

II) Je choisit un groupe de caractères spéciaux

III) Je divise le groupe en deux groupes:
	groupe A pour générer mes clés de chiffrement
	groupe B pour ajouter des caractères après la subtitution

IV) Je définie mes carcatères spéciaux
	ces caractères auront un groupe de carcatère d'une longeur plus petit

---------------------------------------------------------------------------

Regénèrer vos clés de chiffrement si vous modifier ce fichier !!

"""

from string import ascii_lowercase
from random import shuffle

# I)
espace = " "
caractere_sub = list(ascii_lowercase+espace)
nbr_lettre_sub = len(caractere_sub)


# II)
groupe_caracteres_initial = "".join(open("initpat.txt",'r',encoding='utf-8').readlines())

mileu = int(len(groupe_caracteres_initial)/2)


# III)
groupe_a = groupe_caracteres_initial[:mileu]
groupe_b = groupe_caracteres_initial[mileu:]


# IV)
lettre_special = 'esdntxca'+espace

# Oui je sais cette ligne ne sert à rien, mais c'est quand la personne ne connais pas le type de chiffrement ;)
groupe_b = groupe_b+''.join(caractere_sub)*50+lettre_special*50

longeur_caractere = (5,7)
longeur_lettre_special = (3,4)

nombre_cle = (3,5)

# fa et fb détermine le minimume et maximume
# de nombre de caractère qui peuvent être ajouté
fa,fb = (100,900)



