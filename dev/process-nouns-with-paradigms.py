#!usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy, Ft, os;
from Ft.Xml.Domlette import NonvalidatingReader;
from Ft.Xml.XPath import Evaluate;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin);
sys.stdout = codecs.getwriter('utf-8')(sys.stdout);
sys.stderr = codecs.getwriter('utf-8')(sys.stderr);

unk_gen_sg_count = {};
unk_gen_sg_context = {};
unk_gen_pl_count = {};
unk_gen_pl_context = {};

paradigms = {};
hitparade = {};

if len(sys.argv) < 4: #{
	print 'process-nouns-with-paradigms <hitparade> <dix> <sg file> <pl file>';
	sys.exit(-1);
#}	

for line in file(sys.argv[1]).read().split('\n'): #{
	if len(line) < 2: #{
		continue;
	#}
	row = line.strip().split(' ');
	if len(row) < 2: #{
		continue;
	#}
	freq = int(row[0]);
	token = row[1];
	hitparade[token] = freq;
#}


dictionary = sys.argv[2];

if dictionary == os.path.basename(dictionary): #{
	dictionary = os.getcwd() + '/' + dictionary;
#}

doc = NonvalidatingReader.parseUri('file:///' + dictionary);
path = '/dictionary/pardefs/pardef';

paradigms = {};
#categories = ['__n', '__adj', '__vblex'];
categories = ['__n'];

for node in Ft.Xml.XPath.Evaluate(path, contextNode=doc): #{
        pardef = node.getAttributeNS(None, 'n');

	if pardef.count('__n') < 1 or pardef.count('__np') > 0 or pardef.count('__num') > 0: #{
		continue;
	#}

	if pardef not in paradigms: #{
		paradigms[pardef] = [];
	#}

	for child in Ft.Xml.XPath.Evaluate('.//e', contextNode=node): #{
		for pair in Ft.Xml.XPath.Evaluate('.//p', contextNode=child): #{
			suffix = '';
			left = Ft.Xml.XPath.Evaluate('.//l', contextNode=pair)[0].firstChild;

			if type(left) != type(None): #{
				suffix = left.nodeValue;
			else: #{
				suffix = ''
			#}


			symbols = '';
			right =  Ft.Xml.XPath.Evaluate('.//r', contextNode=pair)[0];
			for sym in Ft.Xml.XPath.Evaluate('.//s', contextNode=right): #{
				symbol = '';
				if type(sym) != type(None): #{
					symbol = sym.getAttributeNS(None, 'n');
				#}
				symbols = symbols + '.' + symbol;
			#}

			paradigms[pardef].append((suffix, symbols));
		#}
	#}
#}

#for pardef in paradigms: #{
#	print pardef , paradigms[pardef];
#}

for line in file(sys.argv[3]).read().split('\n'): #{
	if len(line) < 2: #{
		continue;
	#}
	# <det><def><mf><sp>$ ^sistema/*sistema$ ^edukattiv/edukattiv<adj><m><sg>$

	row = line.split('$ ^');
	#print row;
	
	unknown = row[1].split('/')[0].lower();
	context_gender = row[2].split('><')[1];
	context_surface = row[2].split('/')[0]

	if unknown not in unk_gen_sg_count: #{
		unk_gen_sg_count[unknown] = {};
		unk_gen_sg_context[unknown] = {};
	#}	
	if context_gender not in unk_gen_sg_count[unknown]: #{
		unk_gen_sg_count[unknown][context_gender] = 0;
		unk_gen_sg_context[unknown][context_gender] = [];
	#}	

	unk_gen_sg_count[unknown][context_gender] = unk_gen_sg_count[unknown][context_gender] + 1;
	unk_gen_sg_context[unknown][context_gender].append(context_surface);
#}

for line in file(sys.argv[4]).read().split('\n'): #{
	if len(line) < 2: #{
		continue;
	#}
	# <det><def><mf><sp>$ ^sistema/*sistema$ ^edukattiv/edukattiv<adj><m><sg>$

	row = line.split('$ ^');
	#print row;
	
	unknown = row[1].split('/')[0].lower();
	context_gender = row[2].split('><')[1];
	context_surface = row[2].split('/')[0]

	if unknown not in unk_gen_pl_count: #{
		unk_gen_pl_count[unknown] = {};
		unk_gen_pl_context[unknown] = {};
	#}	
	if context_gender not in unk_gen_pl_count[unknown]: #{
		unk_gen_pl_count[unknown][context_gender] = 0;
		unk_gen_pl_context[unknown][context_gender] = [];
	#}	

	unk_gen_pl_count[unknown][context_gender] = unk_gen_pl_count[unknown][context_gender] + 1;
	unk_gen_pl_context[unknown][context_gender].append(context_surface);
#}

for unknown in unk_gen_sg_count: #{
	for paradigm in paradigms: #{
		if len(paradigms[paradigm]) != 2: #{
			continue;
		#}

		suffix = '';
		if paradigm.count('/') > 0: #{
			suffix = paradigm.split('/')[1].split('_')[0];
		#}

		suffixlen = len(suffix.decode('utf-8'));
		unk_len = len(unknown.decode('utf-8'));

		if suffixlen > 0: #{
			fra = unk_len - suffixlen;
			if unknown.decode('utf-8')[fra:] != suffix: #{
				continue;
			#}
		#}
		fra = unk_len - suffixlen;
		unk_stem = unknown.decode('utf-8')[0:fra].encode('utf-8');

		#print paradigm , unknown , unk_stem, ':' ; 

		paradigm_guessed_singular = unk_stem + paradigms[paradigm][0][0];
		paradigm_guessed_plural = unk_stem + paradigms[paradigm][1][0];

		if paradigm_guessed_singular in unk_gen_sg_count and  paradigm_guessed_plural in unk_gen_pl_count: #{
			sg_count = 0;
			pl_count = 0;
			if paradigm_guessed_singular in hitparade: #{
				sg_count = hitparade[paradigm_guessed_singular];
			#}
			if paradigm_guessed_plural in hitparade: #{
				pl_count = hitparade[paradigm_guessed_plural];
			#}
			

			for gender in unk_gen_sg_count[unknown]: #{
				if paradigms[paradigm][0][1].count('.' + gender + '.'): #{
					print sg_count + pl_count , '\t' , paradigm , '\t' , paradigm_guessed_singular , paradigm_guessed_plural ;
				#}
				#if unknown in hitparade: #{
				#	print paradigm , suffix ,  hitparade[unknown] , '\t' , unk_gen_sg_count[unknown][gender] , '\t' ,  gender , '\t' , unknown , set(unk_gen_sg_context[unknown][gender]);
				#}
			#}
		#}
	#}
#}

#				print paradigm , suffix ,  hitparade[unknown] , '\t' , unk_gen_sg_count[unknown][gender] , '\t' ,  gender , '\t' , unknown , set(unk_gen_sg_context[unknown][gender]);
