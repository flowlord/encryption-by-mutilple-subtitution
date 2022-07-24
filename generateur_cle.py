#!/usr/bin/env python
# coding: utf-8
"""
librairie de clé = keylib
fichier qui contient plusieurs clé de chiffrement

GENESIS KEY
"""

from random import randint,choice
from configs.parametre import*

def gen_caractere(x):
    """
    générateur de groupe de carcatère
    (comme un générateur de mot de passe)
    """
    carac = ''
    for _ in range(x):
        carac = carac+choice(groupe_a)
    return carac


def gen_cle(len_carac_sub):
    """
    Génère les clés avec une longeur choisit

    Exemple:
        KEYX = [('a','⥰Ꮖᣧ㎮⥚⻗ጟⲢ'), ('b','𐊐Ϳקּ࢛'), ('c','ڠᖪᴼૄȪ'),  etc... ]
    """

    cle = ''

    for carac in range(len_carac_sub):
        long_carac = randint(len_caractere[0],len_caractere[1])
        long_carac_spe = randint(longeur_carac_special[0],longeur_carac_special[1])
        
        if carac_sub[carac] in carac_special:
            cle = cle + f"('{carac_sub[carac]}','{gen_caractere(long_carac_spe)}'),"
        else:
            cle = cle + f"('{carac_sub[carac]}','{gen_caractere(long_carac)}'),"

    return '['+cle[:-1]+']'


def gen_liste_cle(key_number):
    """
    Génère une liste de clé
    """

    liste_cle = []

    for i in range(1,key_number+1):
        liste_cle = liste_cle + [f'KEY{str(i)}']

    liste_cle = str(liste_cle)
    liste_cle = liste_cle.replace("'","")

    return liste_cle


def gen_lib_cle(key_number):
    """
    Génère une librairie de clé
    """

    file = open('keylib.py','w',encoding='utf-8')
    
    file.write('# coding: utf-8\n')
    file.write('from random import choice\n')
    
    for number in range(1,key_number+1):

        file.write(f'KEY{number} = {gen_cle(len_carac_sub)}\n')
    
    file.write(f'listkey = {gen_liste_cle(key_number)}')

    file.close()


