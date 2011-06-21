#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

def past_p1_sg(stem, root, vowels):
	return {
		# kiteb; ktibt; past.p1.sg; vblex
		'past.p1.sg' : root[0] + root[1] + vowels[0] + root[2] + 't',
		'past.p1.sg.+probj.p1.pl' : None,
		'past.p1.sg.+probj.p1.sg' : None,
		'past.p1.sg.+probj.p2.pl' : root[0] + root[1] + vowels[0] + root[2] + 'tkom',
		'past.p1.sg.+probj.p2.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tek',
		'past.p1.sg.+probj.p3.f.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tha',
		'past.p1.sg.+probj.p3.m.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tu',
		'past.p1.sg.+probj.p3.pl' : root[0] + root[1] + vowels[0] + root[2] + 'thom',
		}

def past_p2_sg(stem, root, vowels):
	return {
		# kiteb; ktibt; past.p2.sg; vblex
		'past.p2.sg' : root[0] + root[1] + vowels[0] + root[2] + 't',
		'past.p2.sg.+probj.p1.pl' : root[0] + root[1] + vowels[0] + root[2] + 'tna',
		'past.p2.sg.+probj.p1.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tni',
		'past.p2.sg.+probj.p2.pl' : None,
		'past.p2.sg.+probj.p2.sg' : None,
		'past.p2.sg.+probj.p3.f.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tha',
		'past.p2.sg.+probj.p3.m.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tu',
		'past.p2.sg.+probj.p3.pl' : root[0] + root[1] + vowels[0] + root[2] + 'thom',
		}

def past_p3_m_sg(stem, root, vowels):
	return {
		# kiteb; kiteb; past.p3.m.sg; vblex
		# the 'i' here -- is it constant, or based on vowels[0]?
		# (Tried changing it for a dot and grepping through the corpus,
		#  no matches other than 'i', no matches with it empty either)
		'past.p3.m.sg' : stem,
		'past.p3.m.sg.+probj.p1.pl' : root[0] + vowels[0] + root[1] + 'i' + root[2] + 'na',
		'past.p3.m.sg.+probj.p1.sg' : root[0] + vowels[0] + root[1] + 'i' + root[2] + 'ni',
		'past.p3.m.sg.+probj.p2.pl' : root[0] + vowels[0] + root[1] + 'i' + root[2] + 'kom',
		'past.p3.m.sg.+probj.p2.sg' : root[0] + vowels[0] + root[1] + root[2] + 'ek',
		'past.p3.m.sg.+probj.p3.f.sg' : root[0] + vowels[0] + root[1] + 'i' + root[2] + 'ha',
		'past.p3.m.sg.+probj.p3.m.sg' : root[0] + vowels[0] + root[1] + root[2] + 'u',
		'past.p3.m.sg.+probj.p3.pl' : root[0] + vowels[0] + root[1] + 'i' + root[2] + 'hom',
		}
	
def past_p3_f_sg(stem, root, vowels):
	return {
		# kiteb; kitbet; past.p3.f.sg; vblex
		'past.p3.f.sg' : root[0] + vowels[0] + root[1] + root[2] + 'et',
		'past.p3.f.sg.+probj.p1.pl' : root[0] + vowels[0] + root[1] + root[2] + 'itna',
		'past.p3.f.sg.+probj.p1.sg' : root[0] + vowels[0] + root[1] + root[2] + 'itni',
		'past.p3.f.sg.+probj.p2.pl' : root[0] + vowels[0] + root[1] + root[2] + 'itkom',
		'past.p3.f.sg.+probj.p2.sg' : root[0] + vowels[0] + root[1] + root[2] + 'itek',
		'past.p3.f.sg.+probj.p3.f.sg' : root[0] + vowels[0] + root[1] + root[2] + 'itha',
		'past.p3.f.sg.+probj.p3.m.sg' : root[0] + vowels[0] + root[1] + root[2] + 'itu',
		'past.p3.f.sg.+probj.p3.pl' : root[0] + vowels[0] + root[1] + root[2] + 'ithom',
		}

def past_p1_pl(stem, root, vowels):
	return {
		# kiteb; ktibna; past.p1.pl; vblex
		'past.p1.pl' : root[0] + root[1] + vowels[0] + root[2] + 'na',
		'past.p1.pl.+probj.p1.pl' : None,
		'past.p1.pl.+probj.p1.sg' : None,
		'past.p1.pl.+probj.p2.pl' : root[0] + root[1] + vowels[0] + root[2] + 'niekom',
		'past.p1.pl.+probj.p2.sg' : root[0] + root[1] + vowels[0] + root[2] + 'niek',
		'past.p1.pl.+probj.p3.f.sg' : root[0] + root[1] + vowels[0] + root[2] + 'nieha',
		'past.p1.pl.+probj.p3.m.sg' : root[0] + root[1] + vowels[0] + root[2] + 'nieh',
		'past.p1.pl.+probj.p3.pl' : root[0] + root[1] + vowels[0] + root[2] + 'niehom',
		}	


def past_p2_pl(stem, root, vowels):
	return {
		# kiteb; ktibtu; past.p2.pl; vblex
		'past.p2.pl' : root[0] + root[1] + vowels[0] + root[2] + 'tu',
		'past.p2.pl.+probj.p1.pl' : root[0] + root[1] + vowels[0] + root[2] + 'tuna',
		'past.p2.pl.+probj.p1.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tuni',
		'past.p2.pl.+probj.p2.pl' : None,
		'past.p2.pl.+probj.p2.sg' : None,
		'past.p2.pl.+probj.p3.f.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tuha',
		'past.p2.pl.+probj.p3.m.sg' : root[0] + root[1] + vowels[0] + root[2] + 'tuh',
		'past.p2.pl.+probj.p3.pl' : root[0] + root[1] + vowels[0] + root[2] + 'tuhom',
		}

def past_p3_pl(stem, root, vowels):
	return {
		# kiteb; kitbu; past.p3.pl; vblex
		'past.p3.pl' : root[0] + vowels[0] + root[1] + root[2] + 'u',
		'past.p3.pl.+probj.p1.pl' : root[0] + vowels[0] + root[1] + root[2] + 'una',
		'past.p3.pl.+probj.p1.sg' : root[0] + vowels[0] + root[1] + root[2] + 'uni',
		'past.p3.pl.+probj.p2.pl' : root[0] + vowels[0] + root[1] + root[2] + 'ukom',
		'past.p3.pl.+probj.p2.sg' : root[0] + vowels[0] + root[1] + root[2] + 'uk',
		'past.p3.pl.+probj.p3.f.sg' : root[0] + vowels[0] + root[1] + root[2] + 'uha',
		'past.p3.pl.+probj.p3.m.sg' : root[0] + vowels[0] + root[1] + root[2] + 'uh',
		'past.p3.pl.+probj.p3.pl' : root[0] + vowels[0] + root[1] + root[2] + 'uhom',
		}

def pres_p1_sg(stem, root, vowels):
	# kiteb; nikteb; pres.p1.sg; vblex
	return 'n' + vowels[0] + root[0] + root[1] + vowels[1] + root[2]

def pres_p2_sg(stem, root, vowels):
	# kiteb; tikteb; pres.p2.sg; vblex
	return 't' + vowels[0] + root[0] + root[1] + vowels[1] + root[2]

def pres_p3_m_sg(stem, root, vowels):
	# kiteb; jikteb; pres.p3.m.sg; vblex
	return 'j' + vowels[0] + root[0]  + root[1] + vowels[1] + root[2]

def pres_p3_f_sg(stem, root, vowels):
	# kiteb; tikteb; pres.p3.f.sg; vblex
	return 't' + vowels[0] + root[0] + root[1] + vowels[1] + root[2]

def pres_p1_pl(stem, root, vowels):
	# kiteb; niktbu; pres.p1.pl; vblex
	return 'n' + vowels[0] + root[0] + root[1] + root[2] + 'u'

def pres_p2_pl(stem, root, vowels):
	# kiteb; tiktbu; pres.p2.pl; vblex
	return 't' + vowels[0] + root[0] + root[1] + root[2] + 'u'

def pres_p3_pl(stem, root, vowels):
	# kiteb; jiktbu; pres.p3.pl; vblex
	return 'j' + vowels[0] + root[0] + root[1] + root[2] + 'u'

def imp_p2_sg(stem, root, vowels):
	# kiteb; ikteb; imp.p2.sg; vblex
	return vowels[0] + root[0] + root[1] + vowels[1] + root[2]

def imp_p2_pl(stem, root, vowels):
	# kiteb; iktbu; imp.p2.pl; vblex
	return vowels[0] + root[0] + root[1] + root[2] + 'u'

def pp_sg(stem, root, vowels):
	# kiteb; miktub; pp.sg; vblex
	return 'm' + vowels[0] + root[0] + root[1] + 'u' + root[2]

def ger(stem, root, vowels):
	# kiteb; kitba; ger; vblex
	return root[0] + vowels[0] + root[1] + root[2] + 'a'

def main(stem, root, vowels):
	sp = {}

	sp['inf'] = stem
	sp.update(past_p1_sg(stem, root, vowels))
	sp.update(past_p2_sg(stem, root, vowels))
	sp.update(past_p3_m_sg(stem, root, vowels))
	sp.update(past_p3_f_sg(stem, root, vowels))
	sp.update(past_p1_pl(stem, root, vowels))
	sp.update(past_p2_pl(stem, root, vowels))
	sp.update(past_p3_pl(stem, root, vowels))
	sp['pres.p1.sg'] = pres_p1_sg(stem, root, vowels)
	sp['pres.p2.sg'] = pres_p2_sg(stem, root, vowels)
	sp['pres.p3.m.sg'] = pres_p3_m_sg(stem, root, vowels)
	sp['pres.p3.f.sg'] = pres_p3_f_sg(stem, root, vowels)
	sp['pres.p1.pl'] = pres_p1_pl(stem, root, vowels)
	sp['pres.p2.pl'] = pres_p2_pl(stem, root, vowels)
	sp['pres.p3.pl'] = pres_p3_pl(stem, root, vowels)
	sp['imp.p2.sg'] = imp_p2_sg(stem, root, vowels)
	sp['imp.p2.pl'] = imp_p2_pl(stem, root, vowels)
	sp['pp.sg'] = pp_sg(stem, root, vowels)
	sp['ger'] = ger(stem, root, vowels)
	
	return sp


