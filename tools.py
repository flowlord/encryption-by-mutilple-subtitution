#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import makedirs
from random import shuffle


def get_pattern_len(file_name):
	"""
	Get number of character
	get_pattern_len("initpat.txt")
	get_pattern_len("initpat (no unicode version).txt")

	"""
	f = "".join(open(file_name,"r",encoding="utf-8").readlines())
	print(len(f))


def gen_many_keylib(x,keyNumber):
	
	print('[ Generating and writing keylib ... ]\n')

	d = 'keylib lib'
	makedirs(d,exist_ok = True)

	for x in range(1,x+1):
		name = d+"/keylib_" + str(x)+".py"

		file = open(name,'w',encoding='utf-8')
		    
		file.write('# coding: utf-8\n')
		file.write('from random import choice\n\n')
		    
		for number in range(1,keyNumber+1):
			file.write(f'KEY{number} = {keygen(nbr_letter_sub)}\n')
			    
		file.write(f'listkey = {gen_listkey(keyNumber)}\n\n')

		file.write('def getRandomKey():\n')
		file.write('\treturn choice(listkey)')
		
		file.close()

		print(f'{x} keylib generated')


def mixer():
	"""
	mix the order of characters
	example:
		AAAZZZ ---> | mixer(2) | ---> ZAAZAZ
	"""

	init = open('initpat.txt','r',encoding='utf-8').readlines()
	init = "".join(init)
	init = list(init)

	for _ in range(2):
		shuffle(init)

	res = "".join(init)

	f = open('initpat.txt','w',encoding='utf-8')
	f.write(res)
	f.close()


mixer()
#gen_many_keylib(x,x)
#get_pattern_len(file_name)




