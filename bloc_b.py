"""
    II) Bloc B
        Chaque carcatère est substituer.
"""

from configs.parametre import*
from random import choice,randint


try:
    from keylib import listkey
except ModuleNotFoundError:
    from keylib_generator import gen_lib_cle
    gen_lib_cle(randint(nombre_cle[0],nombre_cle[1]))
    from keylib import listkey


def cipher(plain_text):
    """
    Je prend une clé au hazard et substitue les caractères
    
    exemple: a ---> 㻀捩䟃퟉覛
    """
    
    plain_text = plain_text.lower()
    
    key = choice(listkey)

    for carac in range(nbr_lettre_sub):
        plain_text = plain_text.replace(caractere_sub[carac],key[carac][1])
        
    return plain_text


def decipher(coded_msg):
    """
    Déchiffre un message codé.
    """

    for key in listkey:
        for element in range(nbr_lettre_sub):
            coded_msg = coded_msg.replace(key[element][1],caractere_sub[element])
    
    return coded_msg

