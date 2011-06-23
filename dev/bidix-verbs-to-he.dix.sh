#!/bin/bash
echo "    <!-- SECTION: Verbs, converted from n0nick's modified hspell, see dev/hspell-to-dix.sh -->"
GREPS=`mktemp -t greps.XXXXXXXX`;

grep '<r>.*<s n="vblex"/>' apertium-mt-he.mt-he.dix |sed 's%.*<r>\(.*\)<s n="vblex"/>.*%<e lm="\1">%' > "$GREPS"
grep -f "$GREPS" -F dev/he.verbs.dix |\
# add line-break on new lemma:
awk -F'"' '//{if($2 != lm) {lm=$2;print "";} print}'

echo '    <!-- /verbs -->'

rm -f "$GREPS"
