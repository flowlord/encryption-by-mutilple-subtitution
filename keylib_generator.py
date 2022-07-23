#!/usr/bin/env python
# coding: utf-8
"""
librairie de clé = keylib
fichier qui contient plusieurs clé de chiffrement

Tribute to GENESIS KEY ( a la base un logiciel proprietaire et payant ;) )
"""

from random import randint,choice
from configs.parametre import*

def genCaractere(x):
    """
    générateur de groupe de carcatère
    (comme un générateur de mot de passe)
    """
    carac = ''
    for _ in range(x):
        carac = carac+choice(groupe_a)
    return carac


def generateur_cle(nbr_lettre_sub):
    """
    Génère les clés avec une longeur choisit

    Exemple:
        KEYX = [('a','⥰Ꮖᣧ㎮⥚⻗ጟⲢ'), ('b','𐊐Ϳקּ࢛'), ('c','ڠᖪᴼૄȪ'),  etc... ]
    """

    cle = ''

    for carac in range(nbr_lettre_sub):
        long_carac = randint(longeur_caractere[0],longeur_caractere[1])
        long_carac_spe = randint(longeur_lettre_special[0],longeur_lettre_special[1])
        
        if caractere_sub[carac] in lettre_special:
            cle = cle + f"('{caractere_sub[carac]}','{genCaractere(long_carac_spe)}'),"
        else:
            cle = cle + f"('{caractere_sub[carac]}','{genCaractere(long_carac)}'),"

    return '['+cle[:-1]+']'


def generateur_liste_cle(keyNumber):
    """
    Génère une liste de clé
    """

    liste_cle = []

    for i in range(1,keyNumber+1):
        liste_cle = liste_cle + [f'KEY{str(i)}']

    liste_cle = str(liste_cle)
    liste_cle = liste_cle.replace("'","")

    return liste_cle


def gen_lib_cle(keyNumber):
    """
    Génère une librairie de clé
    """

    file = open('keylib.py','w',encoding='utf-8')
    
    file.write('# coding: utf-8\n')
    file.write('from random import choice\n')
    
    for number in range(1,keyNumber+1):

        file.write(f'KEY{number} = {generateur_cle(nbr_lettre_sub)}\n')
    
    file.write(f'listkey = {generateur_liste_cle(keyNumber)}')

    file.close()


