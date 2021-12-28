#!/usr/bin/env python
# coding: utf-8
# KEY GENERATOR
# Encryption key generator with the characters of group a

from random import randint,choice
from gen_init import*


keyNumber = 100


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
    Generates a key according to the length chosen

    Example:
        KEYX = [('a','⥰Ꮖᣧ㎮⥚⻗ጟⲢ'), ('b','𐊐Ϳקּ࢛'), ('c','ڠᖪᴼૄȪ'), ('d','ᑮﺎ'), ('e','Ȱ╻') ... ]
    """

    key = ''

    for charac in range(nbr_letter_sub):
        letter_lenght = randint(8,13)
        freq_letter_lenght = randint(2,3)
        
        if charac_sub[charac] in freq_letter:
            key = key + f"('{charac_sub[charac]}','{getRandCharac(freq_letter_lenght)}'),"
        else:
            key = key + f"('{charac_sub[charac]}','{getRandCharac(letter_lenght)}'),"

    return '['+key[:-1]+']'


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
for generate new encryption keys or overwrite the previous encryption keys to generate new ones
"""
gen_file()

