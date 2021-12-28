#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE (multiple substitution encryption)

Created on Tue Jan 22 10:51:19 2019

@author: FLOW LORD

"""

from MSE import mse_cipher,mse_decipher,check_char,check_word


example_sentence = ['meeting tonight for speak','hello world','see you at night','where do you live',
			'What do you do','see you soon','see you next week','see you on monday',
			'see you tomorrow','have a good weekend','i will do that later',
			'i can talk to you','we can see each other','im afraid im busy then',
            'you can help me do my homework','they are there','so far so good']



# message = input('Write a little message: ')

# if check_char(message) is True:
# 	print('there a character that is not in the charac_sub')
# elif check_word(message) is False:
# 	print('it has a word that is not in the word list')
# else:
# 	print('Encrypted text:\n')
# 	message = mse_cipher(message)
# 	print(message,'\n\n')

# 	print('Text decryption:')
# 	print(mse_decipher(message))


print('Encrypted text:\n')
message = mse_cipher('meeting tonight for speak')
print(message,'\n\n')

print('Text decryption:\n')
print(mse_decipher(message))





