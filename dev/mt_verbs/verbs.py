#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy, time;
import classes;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
reload(sys); sys.setdefaultencoding("utf-8")

FORMAT="speling"
if len(sys.argv)>0 and '--dix' in sys.argv:
	FORMAT="dix"


def format_entry(FORMAT, stem, form, pos, feat):
	if FORMAT=="speling":
		return stem + '; ' + speling[feat] + '; ' + feat + '; ' + pos;
	elif FORMAT=="dix":
		tags = ''.join(['<s n="%s"/>' % tag
				for tag in [pos] + feat.split('.')]);
		return "    <e><p><l>%s</l>\t<r>%s%s</r></p></e>" % (speling[feat],
								 stem,
								 tags);
	else:
		raise(Exception);



if FORMAT=="dix": 
	print '  <section id="verbs" type="standard">';
	print '    <!-- Generated on: ' + time.strftime('%Y-%m-%d %H:%M %Z') + ' -->'; 


for line in file('stems.csv'):
	if len(line) < 2 or line[0] == '#':
		continue
	
	row = line.split(',')
	
	#stem, category, gloss, root, vowels, subclass, checked
	stem = row[0].strip()
	category = row[1].strip()
	root = row[3].strip().split('-')
	vowels = row[4].strip().split('-')
	subclass = row[5].strip() if (len(row) >= 5) else None
	
	# build class name
	classname = category
	if subclass:
		classname = classname + '_' + subclass

	try:
		klass = getattr(classes, classname)
		speling = klass.main(stem, root, vowels)
		
		for feat in speling.keys():
			print format_entry(FORMAT, stem, speling[feat], 'vblex', feat);
			
	except AttributeError:
		print 'MISSING CLASS:', classname
		
	print '' # newline between words


if FORMAT=="dix": print '  </section>';
