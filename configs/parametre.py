#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

I) Je choisit un groupe de caractère que je veut substituer

II) Je choisit un groupe de caractères spéciaux

III) Je divise le groupe en deux groupes:
	groupe A pour générer mes clés de chiffrement
	groupe B pour ajouter des caractères après la substitution

IV) Je définie mes carcatères spéciaux
	ces caractères auront un groupe de carcatère d'une longeur plus petit

---------------------------------------------------------------------------
libre à vous de modifier ce fichier !
faite votre propre version et le montrer à personne !
Regénèrer vos clés de chiffrement si vous modifier ce fichier !!

"""

from string import ascii_lowercase
from random import shuffle

espace = " "
carac_sub = list(ascii_lowercase+espace)
len_carac_sub = len(carac_sub)


groupe_caracteres_initial = "".join(open("groupes_caractere.txt",'r',encoding='utf-8').readlines())

milieu = int(len(groupe_caracteres_initial)/2)

groupe_a = groupe_caracteres_initial[:milieu]
groupe_b = groupe_caracteres_initial[milieu:]

carac_special = 'esywqdntzcapv'+espace

len_caractere = (5,7)
longeur_carac_special = (2,3)

nombre_cle = (5,10)

mini,maxi = 100,300





