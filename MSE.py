# -*- coding: utf-8 -*-
"""
    INPUT --> A --> B --> C --> output

    I) Bloc A
        Le texte est légèrement modifié.

    II) Bloc B
        Chaque caractère est substitué.

    II) Bloc C
        Complexifie le code après la substitution.
"""

from pyperclip import copy
from parametre import*
from random import randint,choice

try:
    from keylib import listkey,getRandomKey
except ModuleNotFoundError:
    from keylib_generator import gen_lib_cle
    gen_lib_cle(randint(nombre_cle[0],nombre_cle[1]))
    from keylib import listkey,getRandomKey

def check_word(text):
    """
    vérifie si un mot est dans la list de mot
    """

    text = text.split(' ')

    v = []

    for element in text:
        if element in liste_mots:
            v = v + [0]
        else:
            v = v + [1]

    if 1 in v:
        return False
    else:
        return True

def check_char(msg):
    """
    vérifie si un caratère est dans la variable caractere_sub
    
    """
    msg = list(msg)
    
    v = []
    
    for ch in msg:
        if ch not in caractere_sub:
            v = v + [0]
    
    return 0 in v

def milieu(char):
    """
    abcd --> nombre de carcatères --> 4 --> 4/2 ---> 2
    """
    return int(len(char)/2)

class Bloc_A():
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

    #-------------------------------

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
            return Bloc_A.C2(word)
        else:
            return Bloc_A.C1(word)

    def remettre_mot(word):
        n = len(word)
        
        if n == 1:
            return word
        elif n%2 == 0:
            return Bloc_A.C2_inv(word)
        else:
            return Bloc_A.C1_inv(word)

    def remettre_phrase(code):
        code = code.split(' ')
        msg = ''
        
        for word in code:
            msg = msg + Bloc_A.remettre_mot(word) + ' '
        
        return msg[:-1]

    def inverser_phrase(msg):
        msg = msg.split(' ')
        code = ''
        
        for word in msg:
            code = code + Bloc_A.inverser_mot(word) + ' '
        
        return code[:-1]

    def complex(plain_text):
        """ 
            Modifie légèrement le text
            example:
                hello word ---> rowdl lehol
        """
        plain_text =  plain_text[::-1]
        plain_text = Bloc_A.inverser_phrase(plain_text)
        return plain_text

    def decomplex(coded_text):
        """ 
            Remet le text dans me bon sens
            example:
                rowdl lehol ---> hello world
        """
        coded_text = Bloc_A.remettre_phrase(coded_text)
        coded_text =  coded_text[::-1]
        return coded_text

class Bloc_B():
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
        
        coded_msg = Bloc_A.decomplex(coded_msg)
        
        return coded_msg

    def decipher(coded_msg):
        """
        Essaie déchiffrer le message
        """
        original_code = coded_msg
        
        for key in listkey:
            for element in range(nbr_lettre_sub):
                coded_msg = coded_msg.replace(key[element][1],caractere_sub[element])
        
        coded_msg = Bloc_A.decomplex(coded_msg)
        
        if check_word(coded_msg) is False:
            return Bloc_B.decipher_basic_reverse(original_code)
        else:
            return coded_msg

class Bloc_C():

    """
        II) Bloc C
            Complexifie le code après la subtitution.
    """

    def blop64(coded_msg):
        """
        Example:
            hello world --> 11 caractères --> imapair --> hello world + caractère aléatoire du group B --> hello world@ --> inverse --> world@hello 
            alex --> 4 caractères --> pair --> inverse --> exal
        """

        if milieu(coded_msg)%2 == 1:
            coded_msg = coded_msg + choice(groupe_b)

        a = coded_msg[:milieu(coded_msg)]
        b = coded_msg[milieu(coded_msg):]

        return b+a

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

def mse_cipher(msg):
    coded  = Bloc_A.complex(msg)
    coded = Bloc_B.cipher(coded)
    coded = Bloc_C.chaos(coded,randint(fa,fb))
    coded = Bloc_C.blop64(coded)
    
    copy(coded)
    return coded

def mse_decipher(coded_msg):
    msg = Bloc_C.blop64(coded_msg)
    msg = Bloc_B.deconfuse(msg)
    msg = Bloc_B.decipher(msg)
    
    return msg

def cycle(msg):
    """
    Renvoie un message quand peut déchiffrer
    "Corrige" un bug inconnu qui fait que lorsque on chiffre
    plusieurs message le programme renvoie des caractères illisibles
    """
    original = msg
    msg = mse_cipher(msg)
    d = mse_decipher(msg)

    while check_char(d) is True:
        msg = mse_cipher(original)
        d = mse_decipher(msg)
    
    return msg



