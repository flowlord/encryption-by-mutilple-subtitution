#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE (multiple substitution encryption)

Created on Tue Jan 22 10:51:19 2019

@author: FLOW LORD

twitter: https://twitter.com/flowlord_

see demo: https://youtu.be/81vH2tkX6cs
		  https://youtu.be/RRgbowrAQ0g

website: https://solarissoftwarebulares.fun/

version: MS3

"""

from MSE import mse_cipher,mse_decipher,check_char,check_word,randint


example_sentences = ['meeting tonight for speak','hello world','see you at night','where do you live',
			'What do you do','see you soon','see you next week','see you on monday',
			'see you tomorrow','have a good weekend','i will do that later',
			'i can talk to you','we can see each other','im afraid im busy then',
            'you can help me do my homework','they are there','so far so good']


print('Encrypted text:\n')
message = mse_cipher('hello world')
print(message,'\n\n')

print('Text decryption:\n')
print(mse_decipher(message))


