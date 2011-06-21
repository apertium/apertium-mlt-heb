#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

# Functions for adding pronoun objects to forms:
def probj_p1_pl(form): return form + 'na'
def probj_p1_sg(form): return form + 'ni'
def probj_p2_pl(form): return form + 'kom'
def probj_p2_sg(form): return form + ('k'
				      if (form.endswith('ie') or form.endswith('u'))
				      else 'ek')
def probj_p3_f_sg(form): return form + 'ha'
def probj_p3_m_sg(form): return form + ('h'
					if (form.endswith('ie') or form.endswith('u'))
					else 'u')
def probj_p3_pl(form): return form + 'hom'

def add_probjs(feats, form):
	return {
		feats + '.+probj.p1.pl' : None if '.p1.' in feats else probj_p1_pl(form),
		feats + '.+probj.p1.sg' : None if '.p1.' in feats else probj_p1_sg(form),
		feats + '.+probj.p2.pl' : None if '.p2.' in feats else probj_p2_pl(form),
		feats + '.+probj.p2.sg' : None if '.p2.' in feats else probj_p2_sg(form),
		feats + '.+probj.p3.f.sg' : probj_p3_f_sg(form),
		feats + '.+probj.p3.m.sg' : probj_p3_m_sg(form),
		feats + '.+probj.p3.pl' : probj_p3_pl(form),
		}
		
def past_p1_sg(stem, root, vowels):
	form = root[0] + root[1] + vowels[0] + root[2] + 't'
	sp = add_probjs('past.p1.sg', form)
	# kiteb; ktibt; past.p1.sg; vblex
	sp['past.p1.sg'] = form
	return sp

def past_p2_sg(stem, root, vowels):
	form = root[0] + root[1] + vowels[0] + root[2] + 't'
	sp = add_probjs('past.p2.sg', form)
	# kiteb; ktibt; past.p2.sg; vblex
	sp['past.p2.sg'] = form
	return sp

def past_p3_m_sg(stem, root, vowels):
	i_form = root[0] + vowels[0] + root[1] + 'i' + root[2]
	form = root[0] + vowels[0] + root[1] + root[2]
	sp = {
		'past.p3.m.sg.+probj.p1.pl' : probj_p1_pl(i_form),
		'past.p3.m.sg.+probj.p1.sg' : probj_p1_sg(i_form),
		'past.p3.m.sg.+probj.p2.pl' : probj_p2_pl(i_form),
		'past.p3.m.sg.+probj.p2.sg' : probj_p2_sg(form),
		'past.p3.m.sg.+probj.p3.f.sg' : probj_p3_f_sg(i_form),
		'past.p3.m.sg.+probj.p3.m.sg' : probj_p3_m_sg(form),
		'past.p3.m.sg.+probj.p3.pl' : probj_p3_pl(i_form),
		}
	# kiteb; kiteb; past.p3.m.sg; vblex
	sp['past.p3.m.sg'] = stem
	return sp
	
def past_p3_f_sg(stem, root, vowels):
	form = root[0] + vowels[0] + root[1] + root[2]
	sp = add_probjs('past.p3.f.sg', form + 'it')
	# kiteb; kitbet; past.p3.f.sg; vblex
	sp['past.p3.f.sg'] = form + 'et' # not vowels[1]+'t' ?
	return sp

def past_p1_pl(stem, root, vowels):
	form = root[0] + root[1] + vowels[0] + root[2] + 'n'
	sp = add_probjs('past.p1.pl', form + 'ie')
	# kiteb; ktibna; past.p1.pl; vblex
	sp['past.p1.pl'] = form + 'a'
	return sp

def past_p2_pl(stem, root, vowels):
	form = root[0] + root[1] + vowels[0] + root[2] + 'tu'
	sp = add_probjs('past.p2.pl', form)
	# kiteb; ktibtu; past.p2.pl; vblex
	sp['past.p2.pl'] = form
	return sp

def past_p3_pl(stem, root, vowels):
	form = root[0] + vowels[0] + root[1] + root[2] + 'u'
	sp = add_probjs('past.p3.pl', form)
	# kiteb; kitbu; past.p3.pl; vblex
	sp['past.p3.pl'] = form
	return sp

def pres_p1_sg(stem, root, vowels):
	# kiteb; nikteb; pres.p1.sg; vblex
	return 'n' + vowels[0] + root[0] + root[1] + vowels[1] + root[2]

def pres_p2_sg(stem, root, vowels):
	i_form = 't' + vowels[0] + root[0] + root[1] + 'i' + root[2]
	short_form = 't' + vowels[0] + root[0] + root[1] + root[2]
	full_form = 't' + vowels[0] + root[0] + root[1] + vowels[1] + root[2]
	sp = {
		'pres.p2.sg.+probj.p1.pl' : probj_p1_pl(i_form),
		'pres.p2.sg.+probj.p1.sg' : probj_p1_sg(i_form),
		'pres.p2.sg.+probj.p2.pl' : None,
		'pres.p2.sg.+probj.p2.sg' : None,
		'pres.p2.sg.+probj.p3.f.sg' : probj_p3_f_sg(i_form),
		'pres.p2.sg.+probj.p3.m.sg' : probj_p3_m_sg(short_form),
		'pres.p2.sg.+probj.p3.pl' : probj_p3_pl(i_form),
		}
	# kiteb; tikteb; pres.p2.sg; vblex
	sp['pres.p2.sg'] = full_form
	return sp

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
	sp.update( past_p1_sg(stem, root, vowels) )
	sp.update( past_p2_sg(stem, root, vowels) )
	sp.update( past_p3_m_sg(stem, root, vowels) )
	sp.update( past_p3_f_sg(stem, root, vowels) )
	sp.update( past_p1_pl(stem, root, vowels) )
	sp.update( past_p2_pl(stem, root, vowels) )
	sp.update( past_p3_pl(stem, root, vowels) )
	sp['pres.p1.sg'] = pres_p1_sg(stem, root, vowels)
	sp.update( pres_p2_sg(stem, root, vowels) )
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


