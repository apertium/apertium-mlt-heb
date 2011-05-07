# DEPRECATED!

vowel = ['a', 'e', 'i', 'o', 'u']; 

def get_vowel_positions(stem): #{
	vowels = {};
	count = 0;
	pos = 0;
	for char in stem: #{
		if char in vowel: #{
			vowels[count] = pos;
			count = count + 1;	
		#}
		pos = pos + 1;
	#}
	return vowels;
#}