#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE (multiple substitution encryption)

Created on Tue Jan 22 10:51:19 2019

@author: FLOW LORD

"""

from MSE import mse_cipher,mse_decipher


example_sentence = ['meeting tonight for speak','hello world','see you at night','where do you live',
			'What do you do','see you soon','see you next week','see you on monday',
			'see you tomorrow','have a good weekend','i will do that later',
			'i can talk to you','we can see each other','im afraid im busy then',
            'you can help me do my homework','they are there','so far so good']


message = example_sentence[0]

message = mse_cipher(message)
print(message,'\n\n')

print(mse_decipher(message))




