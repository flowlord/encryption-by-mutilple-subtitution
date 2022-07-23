#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.  Copyright (C) 2019-2022   Flow.L

"""

	███╗   ███╗  ██████╗ ███████╗
	████╗ ████║ ██╔════╝ ██╔════╝
	██╔████╔██║ ╚█████╗  █████╗
	██║╚██╔╝██║  ╚═══██╗ ██╔══╝
	██║ ╚═╝ ██║ ██████╔╝ ███████╗
	╚═╝     ╚═╝ ╚═════╝  ╚══════╝
	
	MSE (multiple substitution encryption)

	Créer le mardi 22 janvier 2019 à 01:10 

	@author: Flow Lord

	twitter: https://twitter.com/flowlord_

	version name: CRC IV
	
#-----------------------------------------------------------------------------------------
    INPUT --> A --> B --> C --> output

    I) Bloc A
        Le texte est légèrement modifié.

    II) Bloc B
        Chaque caractère est substitué.

    II) Bloc C
        Complexifie le code après la substitution.
"""


__doc__ = """
Uasage:
	
	1) Chiffrer et déchiffrer le message
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


from pyperclip import copy,paste
from parametre import*
from random import randint,choice
from tools import encrypt_keylib,decrypt_keylib,reinitialiser,mixer
import sys


try:
    from keylib import listkey,getRandomKey
except ModuleNotFoundError:
    from keylib_generator import gen_lib_cle
    gen_lib_cle(randint(nombre_cle[0],nombre_cle[1]))
    from keylib import listkey,getRandomKey


def check_char(msg):
    """
    vérifie si un caratère est dans la variable caractere_sub
    
    """
    msg = list(msg)
    
    flag = 0
    
    for c in msg:
        if c not in caractere_sub:
            flag = 1
    
    return flag == 0


def milieu(char):
    """
    abcd --> nombre de carcatères --> 4 --> 4/2 ---> 2
    """
    return int(len(char)/2)


"""
    I) Bloc A
        Le text est légèrement modifier.
"""

"""

SUBDIV 8
-----------

initial --> ab | cd | e (impair)
initial --> ab | cd (pair)

C = combinaison

C1: abcde --> ab | cd | e --> change le sens -->c de ab
C1_inv: fait l'inverse

C2: abcd --> ab | cd --> change le sens --> cdab
C2_inv: fait l'inverse

"""


def C1(t):
    m = milieu(t)
    start = t[:m]
    middle = t[m:-1]
    end = t[-1]
    return middle+end+start


def C1_inv(t):
    m = milieu(t)
    start = t[m+1:]
    middle = t[:m]
    end = t[m]
    return start+middle+end


def C2(t):
    m = milieu(t)
    start = t[:m]
    end = t[m:]
    return end+start


def C2_inv(t):
    m = milieu(t)
    start = t[m:]
    end = t[:m]
    return start+end


def inverser_mot(word):
    n = len(word)
    
    if n == 1:
        return word
    elif n%2 == 0:
        return C2(word)
    else:
        return C1(word)


def remettre_mot(word):
    n = len(word)
    
    if n == 1:
        return word
    elif n%2 == 0:
        return C2_inv(word)
    else:
        return C1_inv(word)


def remettre_phrase(code):
    code = code.split(' ')
    msg = ''
    
    for word in code:
        msg = msg + remettre_mot(word) + ' '
    
    return msg[:-1]


def inverser_phrase(msg):
    msg = msg.split(' ')
    code = ''
    
    for word in msg:
        code = code + inverser_mot(word) + ' '
    
    return code[:-1]


def complex(plain_text):
    """ 
        Modifie légèrement le text
        example:
            hello word ---> rowdl lehol
    """
    plain_text =  plain_text[::-1]
    plain_text = inverser_phrase(plain_text)
    return plain_text


def decomplex(coded_text):
    """ 
        Remet le text dans me bon sens
        example:
            rowdl lehol ---> hello world
    """
    coded_text = remettre_phrase(coded_text)
    coded_text =  coded_text[::-1]
    return coded_text

#-----------------------------------------------------------------------------------------

"""
    II) Bloc B
        Chaque carcatère est subtitué.
"""

def cipher(plain_text):
    """
    Je prend une clé au hazard et subtitue les caractères
    """
    plain_text = plain_text.lower()
    reversed_key = choice([True,False])
    key = getRandomKey()
    
    if reversed_key is True:
        key.reverse()

    for letter in range(nbr_lettre_sub):
        plain_text = plain_text.replace(caractere_sub[letter],key[letter][1])
        
    return plain_text


def deconfuse(code):
    """
    Enlève les carcatères du groupe b
    """
    new_text = ""
    for element in code:
        if element not in groupe_b:
            new_text = new_text + element  
    return new_text


def decipher_basic_reverse(coded_msg):
    """
    Déchiffre le message avec une clé inverser
    """
    for key in listkey:
        key.reverse()
        for element in range(nbr_lettre_sub):
            coded_msg = coded_msg.replace(key[element][1],caractere_sub[element])
    
    coded_msg = decomplex(coded_msg)
    
    return coded_msg


def decipher(coded_msg):
    """
    Essaie déchiffrer le message
    """
    original_code = coded_msg
    
    for key in listkey:
        for element in range(nbr_lettre_sub):
            coded_msg = coded_msg.replace(key[element][1],caractere_sub[element])
    
    coded_msg = decomplex(coded_msg)
    
    if check_char(coded_msg) is False:
        return decipher_basic_reverse(original_code)
    else:
        return coded_msg

#-----------------------------------------------------------------------------------------

"""
    II) Bloc C
        Complexifie le code après la subtitution.
"""


def chaos(plain_text,x):
    """
        Ajoute de manière aléatoire un caractère du groupe_b
        dans le code dans une position au hazard x fois.
    """
    plain_text = list(plain_text)
    
    for _ in range(x):
        getRandCharac = choice(groupe_b)
        pos = randint(0,len(plain_text))
        
        plain_text.insert(pos, getRandCharac)

    plain_text = ''.join(plain_text)
    return plain_text

#-----------------------------------------------------------------------------------------

def mse_cipher(msg):
    coded  = complex(msg)
    coded = cipher(coded)
    coded = chaos(coded,randint(fa,fb))

    copy(coded)
    return coded


def mse_decipher(coded_msg):
    msg = deconfuse(coded_msg)
    msg = decipher(msg)

    return msg

#-----------------------------------------------------------------------------------------



example_phrases = ['meeting tonight for speak','rendez vous ce soir pour parler','hello world','on se voit ce soir','ou habitez vous',
			'que faites vous','a bientot','a la semaine prochaine','je peux te parler','on peut se voir','jusqu ici tout va bien']


def chiffrer_plusieurs_messages(liste):
	for message in liste:
		print(mse_cipher(message),'\n')


def déchiffrer_plusieurs_messages(liste):
	for message in liste:
		print(mse_decipher(message),'\n')


def demo():
	print('Text chiffré:\n')
	message = mse_cipher(choice(example_phrases))
	print(message,'\n\n')

	print('Texte déchiffré:\n')
	print(mse_decipher(message))


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
			print('---------- * DEMO * ----------')
			demo()
		else:
			print('commande invalide')
		
	elif sys.argv[1] in cip:
		print(mse_cipher(sys.argv[2]))
		
	elif sys.argv[1] in dec:
		print(mse_decipher(paste()))
	
	elif sys.argv[1] in cryp:
		encrypt_keylib()
		print('[Clés chiffré]')
		
	elif sys.argv[1] in des:
		decrypt_keylib(paste())
		print('[Clés déchiffré]')
	
	elif sys.argv[1] in reset:
		reinitialiser()
	
	elif sys.argv[1] in mxr:
		mixer()
	
	elif sys.argv[1] in h:
		print(__doc__)


main()

