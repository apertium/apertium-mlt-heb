#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy;
from classes import *;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin);
sys.stdout = codecs.getwriter('utf-8')(sys.stdout);
sys.stderr = codecs.getwriter('utf-8')(sys.stderr);

# SETS 

for line in file('stems.csv'): #{
	if len(line) < 2: #{
		continue;
	#}
	row = line.split(',');

	stem = row[0].strip();
	clas = row[1].strip();
	
	if clas == 'kiteb':
		kiteb.main(stem);
	else:
		print 'MISSING CLASS:', clas
	print ''; # newline between words
#}