#!/usr/bin/env python
# coding: utf-8
# KEY GENERATOR
# Encryption key generator with the characters of group a

from string import ascii_lowercase
from random import randint,choice
import os

# I choose the characters i want to substitute
 
space = ' '
charac_sub = list(ascii_lowercase+space)
nbr_letter_sub = len(charac_sub)


# I get all the characters from initpat.txt
initpat = open('initpat.txt','r',encoding='utf-8').readlines()
initpat = "".join(initpat)

# I take the total character length, divide it in half
m = int(len(initpat)/2)

# I made two character group:
# the group has where I will generate the encryption keys
# group b where I will add characters after encryption
group_a = initpat[:m]
group_b = initpat[m:]


# the most common words in English:
# e,s,d,n,t,r,y,o and spacebar.
freq_letter = 'esdntryo'+space

# authorized word list for encryption
word_lst = open('word_lst.txt','r').readlines()
word_lst = [x.replace('\n','') for x in word_lst]


keyNumber = 500


def getRandCharac(x):
    """
    Get random character in group_a x times.
    like password generator
    """
    charac = ''
    for e in range(x):
        charac = charac+choice(group_a)
    return charac


def keygen(nbr_letter_sub):
    """

    """
    key = ''

    for charac in range(nbr_letter_sub):
        letter_lenght = randint(4,10)
        freq_letter_lenght = randint(2,3)
        
        if charac_sub[charac] in freq_letter:
            key = key + f"('{charac_sub[charac]}','{getRandCharac(freq_letter_lenght)}'), "
        else:
            key = key + f"('{charac_sub[charac]}','{getRandCharac(letter_lenght)}'), "

    return '['+key[:-2]+']'


def gen_listkey():
    listkey = []
    for i in range(1,keyNumber+1):
        listkey = listkey + [f'KEY{str(i)}']
    listkey = str(listkey)
    listkey = listkey.replace("'","")
    return listkey


def gen_file():
    """
    Generate encryption keys in a python file
    """
    file = open('keylib.py','w',encoding='utf-8')
    print('[ Generating and writing key ... ]\n')
    slach = '▨'
    
    file.write('# coding: utf-8\n')
    file.write('from random import choice\n\n')
    
    for number in range(1,keyNumber+1):
        print(number,slach+'\n')
        slach = slach+'▨'
        file.write(f'KEY{number} = {keygen(nbr_letter_sub)}\n')
    
    file.write(f'listkey = {gen_listkey()}\n\n')

    file.write('def getRandomKey():\n')
    file.write('\treturn choice(listkey)')
    file.close()

    print('keylib.py Generated')


"""
For overwrite the previous encryption keys to generate new ones
"""
# gen_file()




