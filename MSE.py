# -*- coding: utf-8 -*-
"""

I) Block A
    the messages are slightly modified by functions.

II) Block B
    Each character of the message is substituted by a group
    of randomly generated characters.

III) Block C
    characters of group b are chosen randomly
    and are added to the already encoded message.

"""


from pyperclip import copy
from gen_init import*
from random import randint,choice
from keylib import listkey,getRandomKey


def revlst(key):
    """
    Reverses the elements of a list (here an encryption key)
    so the last item in the list will be the first.
    
    KEYX = ['a','b','c'] ---> KEYX = ['c', 'b', 'a']
    
    """
    new_list = []
    for elment in reversed(key):
        new_list = new_list+[elment]
        
    return new_list


def check_word(text):
    """
    Check if a word is in the word list
    """

    text = text.split(' ')

    v = []

    for element in text:
        if element in word_lst:
            v = v + [0]
        else:
            v = v + [1]

    if 1 in v:
        return False
    else:
        return True


def check_char(msg):
    """
    return True if he has a character
    which is not in the charac_sub list'
    
    """
    msg = list(msg)
    
    v = []
    
    for ch in msg:
        if ch not in charac_sub:
            v = v + [0]
    
    return 0 in v


def get_len(char):
    return int(len(char)/2)


class Block_A():

    def rev(plain_text):
        """
        Reverse the raw text.
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
            return Block_A.a(word)
        else:
            return Block_A.b(word)


    def d(word):
        n = len(word)
        
        if n == 1:
            return word
        elif n%2 == 0:
            return Block_A.a1(word)
        else:
            return Block_A.b1(word)

    def sub_sentence(msg):
        msg = msg.split(' ')
        code = ''
        
        for word in msg:
            code = code + Block_A.c(word) + ' '
        
        return code[:-1]


    def desub_sentence(code):
        code = code.split(' ')
        msg = ''
        
        for word in code:
            msg = msg + Block_A.d(word) + ' '
        
        return msg[:-1]


#----------------------------------------------------------------------
    
    def complicate(plain_text):
        """ complicates the raw text
            example:
                hello word ---> rowdl lehol
        """
        plain_text =  Block_A.rev(plain_text)
        plain_text = Block_A.sub_sentence(plain_text)
        return plain_text


    def decomplex(plain_text):
        """ inverse function of complicate
            example:
                rowdl lehol ---> hello world
        """
        plain_text = Block_A.desub_sentence(plain_text)
        plain_text =  Block_A.rev(plain_text)
        return plain_text


class Block_B():
    """
    II) Block B
        Each character of the message is substituted by a group
        of randomly generated characters.
    """

    def cipher(plain_text):
        plain_text = plain_text.lower()
        
        reversed_key = choice([True,False])
        
        key = getRandomKey()
        
        if reversed_key is True:
            key = revlst(key)
        
        for letter in range(nbr_letter_sub):
            plain_text = plain_text.replace(charac_sub[letter],key[letter][1])
            
        del key    
        
        copy(plain_text)
        return plain_text
    

    def deconfuse(code):
        """
        create a new character string without the 
        characters that are in anti_pat
        """
        new_text = ""
        for element in code:
            if element not in group_b:
                new_text = new_text + element  
        return new_text


    def decipher_basic_reverse(coded_msg):

        for key in listkey:
            key = revlst(key)
            for element in range(nbr_letter_sub):
                coded_msg = coded_msg.replace(key[element][1],charac_sub[element])
        
        coded_msg = Block_A.decomplex(coded_msg)
        
        return coded_msg


    def decipher(coded_msg):
        original_code = coded_msg
        
        
        for key in listkey:
            for element in range(nbr_letter_sub):
                coded_msg = coded_msg.replace(key[element][1],charac_sub[element])
        
        coded_msg = Block_A.decomplex(coded_msg)
        
        if check_word(coded_msg) is False:
            return Block_B.decipher_basic_reverse(original_code)
        else:
            return coded_msg


class Block_C():

    def blop64(coded_msg):
        """
        Example:
            XXXOOOO --> odd length --> XXXOOOO + P --> OOOPXXXO
            XXXOOO --> even length --> OOOXXX
        """

        if get_len(coded_msg)%2 == 1:
            coded_msg = coded_msg + choice(group_b)

        a = coded_msg[:get_len(coded_msg)]
        b = coded_msg[get_len(coded_msg):]

        return b+a
    

    def chaos(plain_text,x):
        """Add randomly characters from group_b to plain_text
          in a randomly chosen position, x times.
        """
        plain_text = list(plain_text)
        
        for _ in range(x):
            getRandCharac = choice(group_b)
            pos = randint(0,len(plain_text))
            
            plain_text.insert(pos, getRandCharac)

        plain_text = ''.join(plain_text)
        return plain_text


def mse_cipher(msg):
    coded  = Block_A.complicate(msg)
    coded = Block_B.cipher(coded)
    coded = Block_C.chaos(coded,randint(100,500))
    coded = Block_C.blop64(coded)
    
    return coded


def mse_decipher(coded_msg):
    msg = Block_C.blop64(coded_msg)
    msg = Block_B.deconfuse(msg)
    msg = Block_B.decipher(msg)
    
    return msg


