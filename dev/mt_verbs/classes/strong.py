def past_p1_sg(stem, root, vowels):
	# kiteb; ktibt; past.p1.sg; vblex
	return root[0] + root[1] + 'i' + root[2] + 't'

def past_p3_m_sg(stem, root, vowels):
	return stem
	
def past_p3_f_sg(stem, root, vowels):
	# kiteb; kitbet; past.p3.f.sg; vblex
	return root[0] + vowels[0] + root[1] + root[2] + 'et'

def past_p1_pl(stem, root, vowels):
	# kiteb; ktibna; past.p1.pl; vblex
	return root[0] + root[1] + 'i' + root[2] + 'na'

def past_p2_pl(stem, root, vowels):
	# kiteb; ktibtu; past.p2.pl; vblex
	return root[0] + root[1] + 'i' + root[2] + 'tu'

def past_p3_pl(stem, root, vowels):
	# kiteb; kitbu; past.p3.pl; vblex
	return root[0] + vowels[0] + root[1] + root[2] + 'u'

def pres_p1_sg(stem, root, vowels):
	# kiteb; nikteb; pres.p1.sg; vblex
	return 'ni' + root[0] + root[1] + vowels[1] + root[2]

def pres_p2_sg(stem, root, vowels):
	# kiteb; tikteb; pres.p2.sg; vblex
	return 'ti' + root[0] + root[1] + vowels[1] + root[2]

def pres_p3_m_sg(stem, root, vowels):
	# kiteb; jikteb; pres.p3.m.sg; vblex
	return 'ji' + root[0]  + root[1] + vowels[1] + root[2]

def pres_p3_f_sg(stem, root, vowels):
	# kiteb; tikteb; pres.p3.f.sg; vblex
	return 'ti' + root[0] + root[1] + vowels[1] + root[2]

def pres_p1_pl(stem, root, vowels):
	# kiteb; niktbu; pres.p1.pl; vblex
	return 'ni' + root[0] + root[1] + root[2] + 'u'

def pres_p2_pl(stem, root, vowels):
	# kiteb; tiktbu; pres.p2.pl; vblex
	return 'ti' + root[0] + root[1] + root[2] + 'u'

def pres_p3_pl(stem, root, vowels):
	# kiteb; jiktbu; pres.p3.pl; vblex
	return 'ji' + root[0] + root[1] + root[2] + 'u'

def imp_p2_sg(stem, root, vowels):
	# kiteb; ikteb; imp.p2.sg; vblex
	return 'i' + root[0] + root[1] + vowels[1] + root[2]

def imp_p2_pl(stem, root, vowels):
	# kiteb; iktbu; imp.p2.pl; vblex
	return 'i' + root[0] + root[1] + root[2] + 'u'

def pp_sg(stem, root, vowels):
	# kiteb; miktub; pp.sg; vblex
	return 'mi' + root[0] + root[1] + 'u' + root[2]

def ger(stem, root, vowels):
	# kiteb; kitba; ger; vblex
	return root[0] + 'i' + root[1] + root[2] + 'a'

def main(stem, root, vowels):
	sp = {}

	sp['inf'] = stem;
	sp['past.p1.sg'] = past_p1_sg(stem, root, vowels);
	sp['past.p2.sg'] = past_p1_sg(stem, root, vowels);
	sp['past.p3.m.sg'] = past_p3_m_sg(stem, root, vowels);
	sp['past.p3.f.sg'] = past_p3_f_sg(stem, root, vowels);
	sp['past.p1.pl'] = past_p1_pl(stem, root, vowels);
	sp['past.p2.pl'] = past_p2_pl(stem, root, vowels);
	sp['past.p3.pl'] = past_p3_pl(stem, root, vowels);
	sp['pres.p1.sg'] = pres_p1_sg(stem, root, vowels);
	sp['pres.p2.sg'] = pres_p2_sg(stem, root, vowels);
	sp['pres.p3.m.sg'] = pres_p3_m_sg(stem, root, vowels);
	sp['pres.p3.f.sg'] = pres_p3_f_sg(stem, root, vowels);
	sp['pres.p1.pl'] = pres_p1_pl(stem, root, vowels);
	sp['pres.p2.pl'] = pres_p2_pl(stem, root, vowels);
	sp['pres.p3.pl'] = pres_p3_pl(stem, root, vowels);
	sp['imp.p2.sg'] = imp_p2_sg(stem, root, vowels);
	sp['imp.p2.pl'] = imp_p2_pl(stem, root, vowels);
	sp['pp.sg'] = pp_sg(stem, root, vowels);
	sp['ger'] = ger(stem, root, vowels);
	
	return sp