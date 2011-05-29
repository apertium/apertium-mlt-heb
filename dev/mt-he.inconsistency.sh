#!/bin/bash

DEV=$(dirname $0)
TMP=/tmp
ALPHABET="ABĊDEFĠGGHĦIIJKLMNOPQRSTUVWXZŻabċdefġgħghieiejklmnopqrstuvwxzżycYCáéíóúàèìòù"
# alphabet of LANG1 (not LANG2), used to ignore punctuation, regexes etc.

LANG1=mt
LANG2=he
PREFIX=$LANG1-$LANG2
BASENAME=apertium-$PREFIX

ANADIX=${DEV}/../${BASENAME}.${LANG1}.dix
transfer () {
    apertium-pretransfer | apertium-transfer ${DEV}/../${BASENAME}.${PREFIX}.t1x  ${DEV}/../${PREFIX}.t1x.bin  ${DEV}/../${PREFIX}.autobil.bin;
}
GENBIN=${DEV}/../${PREFIX}.autogen.bin

# Find all forms and analyses of the source dictionary:
lt-expand $ANADIX |\
        # Print analysis, but only of lines like "form:lemma<tag>" or "form:>:lemma<tag>" (characters 'm' and 'l' are in $ALPHABET)
        # turning analysis into the format ^lemma<tag>$
        awk -vPATTERN="[$ALPHABET]:(>:)?[$ALPHABET]" -F':|:>:' '$0 ~ PATTERN { gsub("/","\\/",$2); print "^" $2 "$ ^.<sent>$"; }' |\
                              tee $TMP/${PREFIX}_testvoc1 |\
        transfer            | tee $TMP/${PREFIX}_testvoc2 |\
        lt-proc -d $GENBIN  >     $TMP/${PREFIX}_testvoc3

# Output:
paste -d _ $TMP/${PREFIX}_testvoc1 $TMP/${PREFIX}_testvoc2 $TMP/${PREFIX}_testvoc3 |\
        sed 's/\^.<sent>\$//g' | sed 's/_/   --------->  /g' | sed 's/\\//g' | sed 's/ \.$//'

# Remove temp files:
rm -f $TMP/${PREFIX}_testvoc1 $TMP/${PREFIX}_testvoc2 $TMP/${PREFIX}_testvoc3
