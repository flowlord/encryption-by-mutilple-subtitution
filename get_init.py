from string import ascii_lowercase

# I choose the characters i want to substitute

space = ' '
charac_sub = ascii_lowercase+space
nbr_letter_sub = len(charac_sub)


# I get all the characters from initpat.txt
initpat = open('initpat.txt','r',encoding='utf-8').readlines()
initpat = "".join(initpat)

# I take the total character length, divide it in half
m = int(len(initpat)/2)

# I made two character group:
# the group has where I will generate the encryption keys
# group b where I will add characters after encryption
GA = initpat[:m]
GB = initpat[m:]


# the most common words in English:
# e,s,d,n,t,r,y,o et l'espace.
freq_letter = 'esdntryo'+space

# authorized word list for encryption
word_lst = open('word_lst.txt','r').readlines()
word_lst = [x.replace('\n','') for x in word_lst]




