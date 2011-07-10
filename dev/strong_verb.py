#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin);
sys.stdout = codecs.getwriter('utf-8')(sys.stdout);
sys.stderr = codecs.getwriter('utf-8')(sys.stderr);

def sym(syms): #{
	return '<s n="' + syms.replace('.', '"/><s n="') + '"/>';
#}

def header(): #{
	header = '';
	header = header + '<dictionary>\n';
	header = header + '  <alphabet>ABĊDEFĠGGHĦIIJKLMNOPQRSTUVWXZŻabċdefġgħghieiejklmnopqrstuvwxzżycYCáéíóúàèìòùñöëäïüçÿāēīōūăĕĭŏŭãẽĩõũ</alphabet>\n';
	header = header + '  <sdefs>\n';
	header = header + '    <sdef n="vblex"/>\n';
	header = header + '    <sdef n="past"/>\n';
	header = header + '    <sdef n="neg"/>\n';
	header = header + '    <sdef n="pres"/>\n';
	header = header + '    <sdef n="imp"/>\n';
	header = header + '    <sdef n="pprs"/>\n';
	header = header + '    <sdef n="pp"/>\n';
	header = header + '    <sdef n="p1"/>\n';
	header = header + '    <sdef n="p2"/>\n';
	header = header + '    <sdef n="p3"/>\n';
	header = header + '    <sdef n="sg"/>\n';
	header = header + '    <sdef n="pl"/>\n';
	header = header + '    <sdef n="m"/>\n';
	header = header + '    <sdef n="f"/>\n';
	header = header + '    <sdef n="mf"/>\n';
	header = header + '  </sdefs>\n';
	header = header + '  <section id="main" type="standard">\n';
	
	return header;
	
#}
 
def footer(): #{
	footer = '';
	footer = footer + '  </section>\n';
	footer = footer + '</dictionary>\n';
	
	return footer;
#}

##-----------------------------------------------------------------------------##

# KaTaB		qasam, waqaf, qara(j), ġara(j), 
# KaTeB		qabeż, ħareġ
# KeTeB		xegħel, fehem, qered
# KeTaB		seraq, wera(j), ġema', ġama'
# KiTeB		kiser, wiżen
# KoToB		qorob, għolob
# KoTaB		għola(j), għoxa(j), ħola(j)

def pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = (pref + r[0] + r[1] + 'u' + r[2], '-') ;
	forms['pp.f.sg'] = (pref + r[0] + r[1] + 'u' + r[2] + 'a', '-') ;
	forms['pp.mf.pl'] = (pref + r[0] + r[1] + 'u' + r[2] + 'in', '-') ;

	return forms;
#}

def pprs(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pprs.m.sg'] = (r[0] + 'ie' + r[1] + 'e' + r[2] , '-') ;
	forms['pprs.f.sg'] = (r[0] + 'ie' + r[1] + r[2] + 'a' , '-') ;
	forms['pprs.mf.pl'] = (r[0] + 'ie' + r[1] + r[2] + 'in' , '-') ;

	return forms;
#}

def imp(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels
	
	forms = {};

	forms['imp.p2.sg'] = (v[0] + r[0] + r[1] + v[1] + r[2], '-');
	forms['imp.p2.pl'] = (v[0] + r[0] + r[1] + r[2] + 'u', '-');

	return forms ; 
#}

def pres(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pres.p3.m.sg'] = ('j' + v[0] + r[0] + r[1] + v[1] + r[2], '-') ;
	forms['pres.p3.f.sg'] = ('t' + v[0] + r[0] + r[1] + v[1] + r[2], '-') ;
	forms['pres.p2.sg'] = ('t' + v[0] + r[0] + r[1] + v[1] + r[2], '-') ;
	forms['pres.p1.sg'] = ('n' + v[0] + r[0] + r[1] + v[1] + r[2], '-') ;
	
	forms['pres.p3.pl'] = ('j' + v[0] + r[0] + r[1] + v[1] + r[2] + 'u', '-') ;
	forms['pres.p2.pl'] = ('t' + v[0] + r[0] + r[1] + v[1] + r[2] + 'u', '-') ;
	forms['pres.p1.pl'] = ('n' + v[0] + r[0] + r[1] + v[1] + r[2] + 'u', '-') ;

	# When the seond radical of the verb is 'l', 'm', 'n' or 'għ', a euphonic 
	# vowel must be inserted

	return forms;
#}

def past(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[2] == 'j' or r[2] == 'għ': #{
		r[2] = '';
	#}

	forms = {};

	forms['past.p3.m.sg'] = (r[0] + v[0] + r[1] + v[1] + r[2], '-'); # Same as stem
	forms['past.p3.f.sg'] = (r[0] + v[0] + r[1] + r[2] + 'et', '-');	# Omit second vowel of stem word
	
	forms['past.p2.sg'] = (r[0] + r[1] + v[1] + r[2] + 't', '-');	# Omit first vowel of stem word
	forms['past.p1.sg'] = (r[0] + r[1] + v[1] + r[2] + 't', '-');	# Omit first vowel of stem word

	forms['past.p3.pl'] = (r[0] + v[0] + r[1] + r[2] + 'u', '-');	# Omit second vowel of stem word
	forms['past.p2.pl'] = (r[0] + r[1] + v[1] + r[2] + 'tu', '-');	# Omit first vowel of stem word
	forms['past.p1.pl'] = (r[0] + r[1] + v[1] + r[2] + 'na', '-');	# Omit first vowel of stem word

	# == Overrides == 

	if r[0] == 'w' or r[0] == 'għ': #{
		# If the first radical is 'w' or 'għ' then we have a full disyllabic form
		forms['past.p2.sg'] = (r[0] + v[0] + r[1] + v[1] + r[2] + 't', '-');	
		forms['past.p1.sg'] = (r[0] + v[0] + r[1] + v[1] + r[2] + 't', '-');	
	#}


	return forms;
#}

##-----------------------------------------------------------------------------##

iv_with_pprs = ['qagħad', 'raqad'];

stems = [
	{'stem': 'qasam', 'gloss': 'break', 'root': 'q-s-m', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv'},
	{'stem': 'ħabat', 'gloss': 'strike', 'root': 'ħ-b-t', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'TD'},
	{'stem': 'ħaqar', 'gloss': 'oppress', 'root': 'ħ-q-r', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'TD'},
	{'stem': 'ħalaq', 'gloss': 'create', 'root': 'ħ-l-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'TD'},
	{'stem': 'ħaraq', 'gloss': 'burn', 'root': 'ħ-r-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'TD'},
	{'stem': 'ħataf', 'gloss': 'snatch', 'root': 'ħ-t-f', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'TD'},
	{'stem': 'għalaq', 'gloss': 'shut', 'root': 'għ-l-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'TD', 'pp': 'ma'},
	{'stem': 'għasar', 'gloss': 'squeeze', 'root': 'għ-s-r', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'TD'},
	{'stem': 'għażaq', 'gloss': 'dig', 'root': 'għ-ż-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'TD'},
	{'stem': 'bagħat', 'gloss': 'send', 'root': 'b-għ-t', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'ċaħad', 'gloss': 'deny', 'root': 'ċ-ħ-d', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'daħak', 'gloss': 'laugh', 'root': 'd-ħ-k', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'dalam', 'gloss': 'grow·dark', 'root': 'd-l-m', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'iv'},
	{'stem': 'fadal', 'gloss': 'be·left·over', 'root': 'f-d-l', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'iv'},
	{'stem': 'fasad', 'gloss': 'bleed', 'root': 'f-s-d', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'iv'},
	{'stem': 'laħaq', 'gloss': 'reach', 'root': 'l-ħ-q', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'iv'},
	{'stem': 'lagħab', 'gloss': 'play', 'root': 'l-għ-b', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'lagħaq', 'gloss': 'lick', 'root': 'l-għ-q', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'marad', 'gloss': 'fall·sick', 'root': 'm-r-d', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'sahar', 'gloss': 'work·overtime', 'root': 's-h-r', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'taħan', 'gloss': 'grind', 'root': 't-ħ-n', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'wasal', 'gloss': 'arrive', 'root': 'w-s-l', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'daħal', 'gloss': 'enter', 'root': 'd-ħ-l', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'ġabar', 'gloss': 'collect', 'root': 'ġ-b-r', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'saħan', 'gloss': 'become·warm', 'root': 's-ħ-n', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'talab', 'gloss': 'pray, ask', 'root': 't-l-b', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'maxat', 'gloss': 'comb', 'root': 'm-x-t', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'qagħad', 'gloss': 'stand', 'root': 'q-għ-d', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'iv', 'pp': 'ma'},
	{'stem': 'bagħad', 'gloss': 'hate', 'root': 'b-għ-d', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'baram', 'gloss': 'twist', 'root': 'b-r-m', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'ħanaq', 'gloss': 'make', 'root': 'ħ-n-q', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'laqat', 'gloss': 'hit', 'root': 'l-q-t', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'qaras', 'gloss': 'pinch', 'root': 'q-r-s', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'rabat', 'gloss': 'tie, bind', 'root': 'r-b-t', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD', 'pp': 'ma'},
	{'stem': 'raqad', 'gloss': 'sleep', 'root': 'r-q-d', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'iv'}, # with pprs ??
	{'stem': 'qara', 'gloss': 'read', 'root': 'q-r-j', 'vowel_perf': 'a-a', 'trans': 'TD'},
	{'stem': 'ġara', 'gloss': 'happen', 'root': 'ġ-r-j', 'vowel_perf': 'a-a', 'trans': 'TD'},
	{'stem': 'ħareġ', 'gloss': 'go·out', 'root': 'ħ-r-ġ', 'vowel_perf': 'a-e', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'ħadem', 'gloss': 'work', 'root': 'ħ-d-m', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'ħafer', 'gloss': 'forgive', 'root': 'ħ-f-r', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'ħaleb', 'gloss': 'milk', 'root': 'ħ-l-b', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'ħalef', 'gloss': 'swear', 'root': 'ħ-l-f', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'għalef', 'gloss': 'feed·animals', 'root': 'għ-l-f', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'ħasel', 'gloss': 'wash', 'root': 'ħ-s-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD', 'pp': 'ma'},
	{'stem': 'għamel', 'gloss': 'make', 'root': 'għ-m-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'qabel', 'gloss': 'agree', 'root': 'q-b-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'qabeż', 'gloss': 'jump', 'root': 'q-b-ż', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'għażel', 'gloss': 'choose', 'root': 'għ-ż-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'qatel', 'gloss': 'kill', 'root': 'q-t-l', 'vowel_perf': 'a-e', 'vowel_impf': 'o-o', 'trans': 'TD', 'pp': 'ma'},
	{'stem': 'ħeles', 'gloss': 'deliver', 'root': 'ħ-l-s', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'me'}, # also iv ?
	{'stem': 'għereq', 'gloss': 'stink', 'root': 'għ-r-q', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'hemeż', 'gloss': 'fasten·with·pin', 'root': 'h-m-ż', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'heġem', 'gloss': 'devour', 'root': 'h-ġ-m', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'hebeż', 'gloss': 'recede', 'root': 'h-b-ż', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'heres', 'gloss': 'pestle', 'root': 'h-r-s', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'ħebel', 'gloss': 'rave', 'root': 'ħ-b-l', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'ħemer', 'gloss': 'ferment', 'root': 'ħ-m-r', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'ħerek', 'gloss': 'rise·early', 'root': 'ħ-r-k', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'deher', 'gloss': 'appear', 'root': 'd-h-r', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'fehem', 'gloss': 'understand', 'root': 'f-h-m', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'xeher', 'gloss': 'wail', 'root': 'x-h-r', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'xegħel', 'gloss': 'light', 'root': 'x-għ-l', 'vowel_perf': 'e-e', 'trans': 'iv'},
	{'stem': 'resaq', 'gloss': 'approach', 'root': 'r-s-q', 'vowel_perf': 'e-a', 'vowel_impf': 'e-a', 'trans': 'TD'},
	{'stem': 'feraħ', 'gloss': 'rejoice', 'root': 'f-r-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'refa', 'gloss': 'raise', 'root': 'r-f-għ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD', 'pp': 'me'},# check impf_v
	{'stem': 'fetaħ', 'gloss': 'open', 'root': 'f-t-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'felaħ', 'gloss': 'be·strong', 'root': 'f-l-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'kesaħ', 'gloss': 'be·cold', 'root': 'k-s-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'mesaħ', 'gloss': 'wipe', 'root': 'm-s-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'lemaħ', 'gloss': 'perceive', 'root': 'l-m-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'rebaħ', 'gloss': 'win', 'root': 'r-b-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'reżaħ', 'gloss': 'shiver', 'root': 'r-ż-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'sebaħ', 'gloss': 'dawn', 'root': 's-b-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'seraq', 'gloss': 'steal', 'root': 's-r-q', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'telaq', 'gloss': 'depart', 'root': 't-l-q', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'selaħ', 'gloss': 'skin', 'root': 's-l-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'żebagħ', 'gloss': 'paint', 'root': 'ż-b-għ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'żelaq', 'gloss': 'slip', 'root': 'ż-l-q', 'vowel_perf': 'e-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'sebaq', 'gloss': 'outstrip', 'root': 's-b-q', 'vowel_perf': 'e-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'nefaħ', 'gloss': 'blow', 'root': 'n-f-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'o-o', 'trans': 'iv'},
	{'stem': 'nefaq', 'gloss': 'spend', 'root': 'n-f-q', 'vowel_perf': 'e-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'beżaq', 'gloss': 'spit', 'root': 'b-ż-q', 'vowel_perf': 'e-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'fetaq', 'gloss': 'unstitch', 'root': 'f-t-q', 'vowel_perf': 'e-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'wera', 'gloss': 'show', 'root': 'w-r-j', 'vowel_perf': 'e-a', 'trans': 'TD'},
	{'stem': 'ġema', 'gloss': 'gather', 'root': 'ġ-m-għ', 'vowel_perf': 'e-a', 'trans': 'TD'},
	{'stem': 'kiser', 'gloss': 'break', 'root': 'k-s-r', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'niżel', 'gloss': 'descend', 'root': 'n-ż-l', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'bidel', 'gloss': 'change', 'root': 'b-d-l', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'difen', 'gloss': 'bury', 'root': 'd-f-n', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'dilek', 'gloss': 'smear', 'root': 'd-l-k', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'fired', 'gloss': 'separate', 'root': 'f-r-d', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'firex', 'gloss': 'spread', 'root': 'f-r-x', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'ġibed', 'gloss': 'pull', 'root': 'ġ-b-d', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'gideb', 'gloss': 'lie', 'root': 'g-d-b', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'gidem', 'gloss': 'bite', 'root': 'g-d-m', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'kiber', 'gloss': 'grow', 'root': 'k-b-r', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'kines', 'gloss': 'sweep', 'root': 'k-n-s', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'giref', 'gloss': 'scratch', 'root': 'g-r-f', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'nidem', 'gloss': 'repent', 'root': 'n-d-m', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'kixef', 'gloss': 'unveil', 'root': 'k-x-f', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD', 'pp': 'mi'},
	{'stem': 'siker', 'gloss': 'get·drunk', 'root': 's-k-r', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'silef', 'gloss': 'lend', 'root': 's-l-f', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'tilef', 'gloss': 'lose', 'root': 't-l-f', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'żifen', 'gloss': 'dance', 'root': 'ż-f-n', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'wiżen', 'gloss': 'weigh', 'root': 'w-ż-n', 'vowel_perf': 'i-e', 'trans': 'TD'},
	{'stem': 'siket', 'gloss': 'be·silent', 'root': 's-k-t', 'vowel_perf': 'i-e', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'sogħol', 'gloss': 'cough', 'root': 's-għ-l', 'vowel_perf': 'o-o', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'sogħob', 'gloss': 'be·sorry', 'root': 's-għ-b', 'vowel_perf': 'o-o', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'xorob', 'gloss': 'drink', 'root': 'x-r-b', 'vowel_perf': 'o-o', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'ħolom', 'gloss': 'dream', 'root': 'ħ-l-m', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'korob', 'gloss': 'groan', 'root': 'k-r-b', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'ħoloq', 'gloss': 'create', 'root': 'ħ-l-q', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'forogħ', 'gloss': 'ebb', 'root': 'f-r-għ', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'kotor', 'gloss': 'abound', 'root': 'k-t-r', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'għodos', 'gloss': 'dive', 'root': 'għ-d-s', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'għokos', 'gloss': 'decay', 'root': 'għ-k-s', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'għorok', 'gloss': 'rub', 'root': 'għ-r-k', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'għolob', 'gloss': 'grow·thin', 'root': 'għ-l-b', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'iv'},
	{'stem': 'qorob', 'gloss': 'get·near', 'root': 'q-r-b', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'iv'}
];

##-----------------------------------------------------------------------------##

infl = {};

for stem in stems: #{

	infl[stem['stem']] = past(stem['root'], stem['vowel_perf']);

	if stem['trans'] == 'tv' or stem['stem'] in iv_with_pprs:
		infl[stem['stem']].update(pprs(stem['root'], stem['vowel_perf']));

	if 'pp' in stem: 
		infl[stem['stem']].update(pp(stem['root'], stem['vowel_perf'], stem['pp']));

	if 'vowel_impf' in stem: 
		infl[stem['stem']].update(pres(stem['root'], stem['vowel_impf']));
		infl[stem['stem']].update(imp(stem['root'], stem['vowel_impf']));
#}

print header();

for stem in infl: #{

	for flex in infl[stem]: #{
		outline = '';
		left = infl[stem][flex][0];
		right = stem + '<s n="vblex"/>' + sym(flex);

		if infl[stem][flex][1] == '-': #{
			outline = outline + '    <e lm="' + stem + '">';
		else: #{
			outline = outline + '    <e lm="' + stem + '" r="' + infl[stem][flex][1] + '">';
		#}
		print outline + '<p><l>' + left + '</l><r>' + right + '</r></p></e>';
		print outline + '<p><l>' + left + 'x</l><r>' + right + '<j/>x<s n="neg"/></r></p></e>';
	#}
#}

print footer();
