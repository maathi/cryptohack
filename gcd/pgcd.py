#!/usr/bin/python

#is this Euclidean algorithm?

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def pgcd(a, b):
	if(b>a):
		x = b
		b = a 
		a = x	
	
	r = a % b

	if(r == 0):
		return b 
	else:
		return pgcd(b, r)

		
print(pgcd(a, b))

