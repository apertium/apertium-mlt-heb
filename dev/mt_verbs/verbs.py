#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy;
import classes;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin);
sys.stdout = codecs.getwriter('utf-8')(sys.stdout);
sys.stderr = codecs.getwriter('utf-8')(sys.stderr);

for line in file('stems.csv'): #{
	if len(line) < 2: #{
		continue;
	#}
	row = line.split(',');

	stem = row[0].strip();
	clas = row[1].strip();
	
	try:
		klass = getattr(classes, clas);
		klass.main(stem);
	except AttributeError:
		print 'MISSING CLASS:', clas
	print ''; # newline between words
#}