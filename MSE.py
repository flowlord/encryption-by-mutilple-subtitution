# -*- coding: utf-8 -*-
"""
    INPUT --> A --> B --> C --> output

    I) Bloc A
        Le text est légèrement modifier.

    II) Bloc B
        Chaque carcatère est subtitué.

    II) Bloc C
        Complexifie le code après la subtitution.

le module pyperclip est nécessaire pour que les
messages codés sois copier automatiquement

pip install pyperclip

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


def inverser_liste(key):
    """
    KEYX = ['a','b','c'] ---> KEYX = ['c', 'b', 'a']
    
    """
    new_list = []
    for element in reversed(key):
        new_list = new_list+[element]
        
    return new_list


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
        if ch not in charac_sub:
            v = v + [0]
    
    return 0 in v


def get_len(char):
    return int(len(char)/2)

class Bloc_A():
    """
        I) Bloc A
        Le text est légèrement modifier.
    """

    def inverser_text(plain_text):
        """
        Inverse le text.
        """
        new_text = ''
        for element in reversed(plain_text):
            new_text = new_text+element
        return new_text

    def b(t):
        
        n = len(t)
        m = int(n/2)
        
        start = t[:m]
        middle = t[m:-1]
        end = t[-1]
        
        return middle+end+start

    def b1(t):
        
        n = len(t)
        m = int(n/2)
        
        start = t[m+1:]
        middle = t[:m]
        end = t[m]
        
        return start+middle+end

#-------------------------------

    def a(t):
        n = len(t)
        m = int(n/2)
        
        start = t[:m]
        end = t[m:]
        
        return end+start

    def a1(t):
        n = len(t)
        m = int(n/2)
        
        start = t[m:]
        end = t[:m]
        
        return start+end


    def c(word):
        n = len(word)
        
        if n == 1:
            return word
        elif n%2 == 0:
            return Bloc_A.a(word)
        else:
            return Bloc_A.b(word)


    def d(word):
        n = len(word)
        
        if n == 1:
            return word
        elif n%2 == 0:
            return Bloc_A.a1(word)
        else:
            return Bloc_A.b1(word)

    def sub_sentence(msg):
        msg = msg.split(' ')
        code = ''
        
        for word in msg:
            code = code + Bloc_A.c(word) + ' '
        
        return code[:-1]


    def desub_sentence(code):
        code = code.split(' ')
        msg = ''
        
        for word in code:
            msg = msg + Bloc_A.d(word) + ' '
        
        return msg[:-1]


    def complex(plain_text):
        """ 
            Modifie légèrement le text
            example:
                hello word ---> rowdl lehol
        """
        plain_text =  Bloc_A.inverser_text(plain_text)
        plain_text = Bloc_A.sub_sentence(plain_text)
        return plain_text


    def decomplex(plain_text):
        """ 
            Remet le text dans me bon sens
            example:
                rowdl lehol ---> hello world
        """
        plain_text = Bloc_A.desub_sentence(plain_text)
        plain_text =  Bloc_A.inverser_text(plain_text)
        return plain_text


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
            key = inverser_liste(key)
        
        for letter in range(nbr_lettre_sub):
            plain_text = plain_text.replace(caractere_sub[letter],key[letter][1])
            
        del key
        
        copy(plain_text)
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
            key = inverser_liste(key)
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
            XXXOOOO --> imapair --> XXXOOOO + P --> OOOPXXXO
            XXXOOO --> pair --> OOOXXX
        """

        if get_len(coded_msg)%2 == 1:
            coded_msg = coded_msg + choice(groupe_b)

        a = coded_msg[:get_len(coded_msg)]
        b = coded_msg[get_len(coded_msg):]

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
    
    return coded


def mse_decipher(coded_msg):
    msg = Bloc_C.blop64(coded_msg)
    msg = Bloc_B.deconfuse(msg)
    msg = Bloc_B.decipher(msg)
    
    return msg



