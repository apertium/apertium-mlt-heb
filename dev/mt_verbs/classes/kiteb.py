# DEPRECATED!

from common import *

def past_p1_sg(stem): #{
	surface = '';
	# kiteb; ktibt; past.p1.sg; vblex

	# delete first vowel
	# change second vowel to 'e'
	# append 't'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		elif i == vowels[1]: #{		## RULE 2: Change second vowel to 'i'
			surface = surface + 'i';
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = surface + 't';		## RULE 3: Append 't'

	return surface;
#}

def past_p3_f_sg(stem): #{
	surface = '';
	# kiteb; kitbet; past.p3.f.sg; vblex

	# delete second vowel
	# append 'et'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = surface + 'et';		## RULE 3: Append 'et'

	return surface;
#}

def past_p1_pl(stem): #{
	surface = ''
	# kiteb; ktibna; past.p1.pl; vblex
	
	# delete first vowel
	# change second vowel to 'i'
	# append 'na'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		elif i == vowels[1]: #{		## RULE 2: Change second vowel to 'i'
			surface = surface + 'i';
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = surface + 'na';		## RULE 3: Append 'na'

	return surface;
#}

def past_p2_pl(stem): #{
	surface = ''
	# kiteb; ktibtu; past.p2.pl; vblex
	
	# delete first vowel
	# change second vowel to 'i'
	# append 'tu'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		elif i == vowels[1]: #{		## RULE 2: Change second vowel to 'i'
			surface = surface + 'i';
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = surface + 'tu';		## RULE 3: Append 'tu'

	return surface;
#}

def past_p3_pl(stem): #{
	surface = ''
	# kiteb; kitbu; past.p3.pl; vblex
	
	# delete second vowel
	# append 'u'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = surface + 'u';		## RULE 2: Append 'u'

	return surface;
#}

def pres_p1_sg(stem): #{
	surface = ''
	# kiteb; nikteb; pres.p1.sg; vblex
	
	# delete first vowel
	# prepend 'ni'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'ni' + surface;		## RULE 2: Prepend 'ni'

	return surface;
#}

def pres_p2_sg(stem): #{
	surface = ''
	# kiteb; tikteb; pres.p2.sg; vblex
	
	# delete first vowel
	# prepend 'ti'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'ti' + surface;		## RULE 2: Prepend 'ti'

	return surface;
#}

def pres_p3_m_sg(stem): #{
	surface = ''
	# kiteb; jikteb; pres.p3.m.sg; vblex
	
	# delete first vowel
	# prepend 'ji'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'ji' + surface;		## RULE 2: Prepend 'ji'

	return surface;
#}

def pres_p3_f_sg(stem): #{
	surface = ''
	# kiteb; tikteb; pres.p3.f.sg; vblex
	
	# delete first vowel
	# prepend 'ti'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'ti' + surface;		## RULE 2: Prepend 'ti'

	return surface;
#}

def pres_p1_pl(stem): #{
	surface = ''
	# kiteb; niktbu; pres.p1.pl; vblex
	
	# delete first vowel
	# delete second vowel
	# prepend 'ni'
	# append 'u'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		if i == vowels[1]: #{		## RULE 2: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'ni' + surface;		## RULE 3: Prepend 'ni'
	surface = surface + 'u';		## RULE 4: Append 'u'

	return surface;
#}

def pres_p2_pl(stem): #{
	surface = ''
	# kiteb; tiktbu; pres.p2.pl; vblex
	
	# delete first vowel
	# delete second vowel
	# prepend 'ti'
	# append 'u'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		if i == vowels[1]: #{		## RULE 2: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'ti' + surface;		## RULE 3: Prepend 'ti'
	surface = surface + 'u';		## RULE 4: Append 'u'

	return surface;
#}

def pres_p3_pl(stem): #{
	surface = ''
	# kiteb; jiktbu; pres.p3.pl; vblex
	
	# delete first vowel
	# delete second vowel
	# prepend 'ji'
	# append 'u'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		if i == vowels[1]: #{		## RULE 2: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'ji' + surface;		## RULE 3: Prepend 'ji'
	surface = surface + 'u';		## RULE 4: Append 'u'

	return surface;
#}

def imp_p2_sg(stem): #{
	surface = ''
	# kiteb; ikteb; imp.p2.sg; vblex
	
	# delete first vowel
	# prepend 'i'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'i' + surface;		## RULE 2: Prepend 'ji'

	return surface;
#}

def imp_p2_pl(stem): #{
	surface = ''
	# kiteb; iktbu; imp.p2.pl; vblex
	
	# delete first vowel
	# delete second vowel
	# prepend 'i'
	# append 'u'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		if i == vowels[1]: #{		## RULE 2: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'i' + surface;		## RULE 3: Prepend 'i'
	surface = surface + 'u';		## RULE 4: Append 'u'

	return surface;
#}

def pp_sg(stem): #{
	surface = ''
	# kiteb; miktub; pp.sg; vblex
	
	# delete first vowel
	# change second vowel to 'u'
	# prepend 'mi'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[0]: #{		## RULE 1: Delete first vowel
			continue;
		elif i == vowels[1]: #{		## RULE 2: Change second vowel to 'u'
			surface = surface + 'u';
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = 'mi' + surface;		## RULE 3: Prepend 'mi'

	return surface;
#}

def ger(stem): #{
	surface = ''
	# kiteb; kitba; ger; vblex
	
	# delete second vowel
	# append 'a'
	
	vowels = get_vowel_positions(stem);
	
	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: delete second vowel
			continue
		else:
			surface = surface + stem[i];
	#}
	surface = surface + 'a'		## RULE 2: Append 'a'
	
	return surface;
#}


def main(stem): #{
	speling_line = {};

	speling_line['inf'] = stem;
	speling_line['past.p1.sg'] = past_p1_sg(stem);
	speling_line['past.p2.sg'] = past_p1_sg(stem);
	speling_line['past.p3.m.sg'] = stem;
	speling_line['past.p3.f.sg'] = past_p3_f_sg(stem);
	speling_line['past.p1.pl'] = past_p1_pl(stem);
	speling_line['past.p2.pl'] = past_p2_pl(stem);
	speling_line['past.p3.pl'] = past_p3_pl(stem);
	speling_line['pres.p1.sg'] = pres_p1_sg(stem);
	speling_line['pres.p2.sg'] = pres_p2_sg(stem);
	speling_line['pres.p3.m.sg'] = pres_p3_m_sg(stem);
	speling_line['pres.p3.f.sg'] = pres_p3_f_sg(stem);
	speling_line['pres.p1.pl'] = pres_p1_pl(stem);
	speling_line['pres.p2.pl'] = pres_p2_pl(stem);
	speling_line['pres.p3.pl'] = pres_p3_pl(stem);
	speling_line['imp.p2.sg'] = imp_p2_sg(stem);
	speling_line['imp.p2.pl'] = imp_p2_pl(stem);
	speling_line['pp.sg'] = pp_sg(stem);
	speling_line['ger'] = ger(stem);

	for feat in speling_line.keys(): #{
		print stem + '; ' + speling_line[feat] + '; ' + feat + '; vblex';
	#}
#}