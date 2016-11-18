#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-11-17 14:44:20
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-11-18 13:03:36

import primefac
from glob import glob
import os

import binascii

os.chdir('encrypted')

files = sorted(glob('*'))

primes = []

for file in files:
	number = int(file)
	# print primefac.isprime(number)
	if ( primefac.isprime(number) ):
		#primes.append(number)
		primes.append( open(file).read().replace('\n','') )

print ''.join([ str(z) for z in primes])