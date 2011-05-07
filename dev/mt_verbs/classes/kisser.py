# DEPRECATED!

from common import *

def past_p1_sg(stem): #{
	surface = '';
	# kisser; kissirt; past.p1.sg; vblex
	
	# change second vowel to 'i'
	# append 't'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: Change second vowel to 'i'
			surface = surface + 'i';
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = surface + 't';		## RULE 2: Append 't'
	
	return surface;
#}
def past_p2_sg(stem): #{
	surface = '';
	# kisser; kissirt; past.p2.sg; vblex
	
	# change second vowel to 'i'
	# append 't'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: Change second vowel to 'i'
			surface = surface + 'i';
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = surface + 't';		## RULE 2: Append 't'
	
	return surface;
#}
def past_p3_f_sg(stem): #{
	surface = '';
	# kisser; kissret; past.p3.f.sg; vblex
	
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
	surface = surface + 'et';		## RULE 2: Append 'et'
	
	return surface;
#}
def past_p1_pl(stem): #{
	surface = '';
	# kisser; kissirna; past.p1.pl; vblex
	
	# change second vowel to 'i'
	# append 'na'

	vowels = get_vowel_positions(stem);

	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: Change second vowel to 'i'
			surface = surface + 'i';
		else: 
			surface = surface + stem[i];
		#}
	#}	
	surface = surface + 'na';		## RULE 2: Append 'na'
	
	return surface;
#}
def past_p2_pl(stem): #{
	surface = '';
	# kisser; kssirtu; past.p2.pl; vblex
	
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
	surface = '';
	# kisser; kissru; past.p3.pl; vblex
	
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
	surface = '';
	# kisser; inkisser; pres.p1.sg; vblex
	
	# prepend 'in'
	
	surface = 'in' + stem;		## RULE 1: Prepend 'in'
	
	return surface;
#}
def pres_p2_sg(stem): #{
	surface = '';
	# kisser; tkisser; pres.p2.sg; vblex
	
	# prepend 't'
	
	surface = 't' + stem;		## RULE 1: Prepend 't'
	
	return surface;
#}
def pres_p3_m_sg(stem): #{
	surface = '';
	# kisser; ikisser; pres.p3.m.sg; vblex
	
	# prepend 'i'
	
	surface = 'i' + stem;		## RULE 1: Prepend 't'
	
	return surface;
#}
def pres_p3_f_sg(stem): #{
	surface = '';
	# kisser; tkisser; pres.p3.f.sg; vblex
	
	# prepend 't'
	
	surface = 't' + stem;		## RULE 1: Prepend 't'
	
	return surface;
#}
def pres_p1_pl(stem): #{
	surface = '';
	# kisser; inkissru; pres.p1.pl; vblex
	
	# delete second vowel
	# prepend 'in'
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
	surface = 'in' + surface;		## RULE 2: Prepend 'in'
	surface = surface + 'u';		## RULE 3: Append 'u'
	
	return surface;
#}
def pres_p2_pl(stem): #{
	surface = '';
	# kisser; tkissru; pres.p2.pl; vblex
	
	# delete second vowel
	# prepend 't'
	
	vowels = get_vowel_positions(stem);
	
	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}
	surface = 't' + surface;		## RULE 2: Prepend 't'
	
	return surface;
#}
def pres_p3_pl(stem): #{
	surface = '';
	# kisser; ikissru; pres.p3.pl; vblex
	
	# delete second vowel
	# prepend 'i'
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
	surface = 'i' + surface;		## RULE 2: Prepend 't'
	surface = surface + 'u';		## RULE 3: Append 'u'
	
	return surface;
#}
def imp_p2_pl(stem): #{
	surface = '';
	# kisser; kissru; imp.p2.pl; vblex
	
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
def pp_m_sg(stem): #{
	surface = '';
	# kisser; imkisser; pp.m.sg; vblex
	
	# prepend 'im'
	
	surface = 'im' + stem;		## RULE 1: Prepend 'im'
	
	return surface;
#}
def pp_f_sg(stem): #{
	surface = '';
	# kisser; imkissra; pp.f.sg; vblex
	
	# delete second vowel
	# prepend 'im'
	# append 'a'
	
	vowels = get_vowel_positions(stem);
	
	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}
	surface = 'im' + surface;		## RULE 2: Prepend 'im'
	surface = surface + 'u';		## RULE 3: Append 'a'
	
	return surface;
#}
def pp_pl(stem): #{
	surface = '';
	# kisser; imkissrin; pp.pl; vblex
	
	# delete second vowel
	# prepend 'im'
	# append 'in'
	
	vowels = get_vowel_positions(stem);
	
	# RULES
	
	for i in range(0, len(stem)): #{
		if i == vowels[1]: #{		## RULE 1: Delete second vowel
			continue;
		else: 
			surface = surface + stem[i];
		#}
	#}
	surface = 'im' + surface;		## RULE 2: Prepend 'im'
	surface = surface + 'in';		## RULE 3: Append 'in'
	
	return surface;
#}

def main(stem): #{
	speling_line = {};
	
	speling_line['inf'] = stem;
	
	speling_line['past.p1.sg'] = past_p1_sg(stem);
	speling_line['past.p2.sg'] = past_p2_sg(stem);
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
	speling_line['imp.p2.sg'] = stem;
	speling_line['imp.p2.pl'] = imp_p2_pl(stem);
	speling_line['pp.m.sg'] = pp_m_sg(stem);
	speling_line['pp.f.sg'] = pp_f_sg(stem);
	speling_line['pp.pl'] = pp_pl(stem);

	for feat in speling_line.keys(): #{
		print stem + '; ' + speling_line[feat] + '; ' + feat + '; vblex';
	#}
#}