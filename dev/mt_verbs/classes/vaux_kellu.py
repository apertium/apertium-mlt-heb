#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

def main(stem, root, vowels):
	sp = {}

	sp['inf'] = stem
	sp['past.p1.sg'] = 'ikolli'
	sp['past.p2.sg'] = 'ikollok' 
	sp['past.p3.m.sg'] = 'ikollu'
	sp['past.p3.f.sg'] = 'ikollha' 
	sp['past.p1.pl'] = 'ikollna'
	sp['past.p2.pl'] = 'ikollkom' 
	sp['past.p3.pl'] = 'ikollhom'
	sp['pres.p1.sg'] = 'kelli'
	sp['pres.p2.sg'] = 'kellek'
	sp['pres.p3.m.sg'] = 'kellu'
	sp['pres.p3.f.sg'] = 'kellha'
	sp['pres.p1.pl'] = 'kellna'
	sp['pres.p2.pl'] = 'kellkom'
	sp['pres.p3.pl'] = 'kellhom'

	nsp = {}
	for f in sp: 
		nsp[f + '.+neg'] = sp[f] + 'x';

	for n in nsp:
		sp[n] = nsp[n];

	return sp

