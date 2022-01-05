#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
If you modify this file you must regenerate your encryption keys
I choose the characters i want to substitute
I get all the characters from initpat.txt
I take the total character length, divide it in half
I made two character group
the group has where I will generate the encryption keys
group b where I will add characters after encryption
the most common words in English:
e,s,d,n,t,r,y and o
[update] why put only frequence letter ?
authorized word list for encryption

"""

from string import ascii_lowercase
from random import shuffle


space = ' '
charac_sub = list(ascii_lowercase+space)
nbr_letter_sub = len(charac_sub)


initpat = open('initpat.txt','r',encoding='utf-8').readlines()
initpat = "".join(initpat)


def mix_initpat(x,initpat):
    """
    I mix special characters from initpat file x times
    """
    initpat = list(initpat)

    for _ in range(x):
        shuffle(initpat)
    
    initpat = "".join(initpat)

    f = open('initpat.txt','w', encoding='utf-8')
    f.write(initpat)
    f.close()


#mix_initpat(2,initpat)


m = int(len(initpat)/2)

group_a = initpat[:m]
group_b = initpat[m:]


freq_letter = 'esdntryo'+'yzxca'+space

#group_b = initpat[m:] + freq_letter*900

word_lst = open('word_lst.txt','r').readlines()
word_lst = [x.replace('\n','') for x in word_lst]



