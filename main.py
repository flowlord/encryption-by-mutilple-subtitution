#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MSE (multiple substitution encryption)

Created on Tue Jan 22 10:51:19 2019

@author: FLOW LORD

"""

from MSE import mse_cipher,mse_decipher

message = 'meeting tonight for speak'

message = mse_cipher(message)
print(message,'\n\n')

print(mse_decipher(message))




