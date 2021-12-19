from string import ascii_lowercase
from random import shuffle

# I choose the characters i want to substitute
 
space = ' '
charac_sub = list(ascii_lowercase+space)
nbr_letter_sub = len(charac_sub)

# I get all the characters from initpat.txt
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

# I take the total character length, divide it in half
m = int(len(initpat)/2)

# I made two character group:
# the group has where I will generate the encryption keys
# group b where I will add characters after encryption
group_a = initpat[:m]
group_b = initpat[m:]


# the most common words in English:
# e,s,d,n,t,r,y and o
# [update] why put only frequence letter ?
freq_letter = 'esdntryo'+'yzxca'+space

# authorized word list for encryption
word_lst = open('word_lst.txt','r').readlines()
word_lst = [x.replace('\n','') for x in word_lst]




