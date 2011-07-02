CORPUS=/home/fran/corpora/maltese/scannell/mt.crp.txt

cat $CORPUS | apertium -d ../ mt-he-morph | grep '<det><def><mf><sp>\$ \^[a-z]\+\/\*[a-z]\+\$ ^[a-z]\+\/[a-z]\+<adj><\(m\|f\)><sg>\$' | sed 's/<det><def><mf><sp>\$ \^[a-z]\+\/\*[a-z]\+\$ ^[a-z]\+\/[a-z]\+<adj><\(m\|f\)><sg>\$/@&@/g' | cut -f2 -d'@' > /tmp/mt-noun-candidates.txt


