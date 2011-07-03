#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

def main(stem, root, vowels):
	sp = {}

	sp['inf'] = stem
	sp['past.p1.sg'] = 'inkun'
	sp['past.p2.sg'] = 'tkun' # thun
	sp['past.p3.m.sg'] = 'ikun'
	sp['past.p3.f.sg'] = 'tkun' #thun
	sp['past.p1.pl'] = 'nkunu'
	sp['past.p2.pl'] = 'tkunu' # tirunu
	sp['past.p3.pl'] = 'ikunu'
	sp['pres.p1.sg'] = 'kont'
	sp['pres.p2.sg'] = 'kont'
	sp['pres.p3.m.sg'] = 'kien'
	sp['pres.p3.f.sg'] = 'kienet'
	sp['pres.p1.pl'] = 'konna'
	sp['pres.p2.pl'] = 'kontu'
	sp['pres.p3.pl'] = 'kienu'

	nsp = {}
	for f in sp: 
		nsp[f + '.+neg'] = sp[f] + 'x';

	for n in nsp:
		sp[n] = nsp[n];

	return sp

