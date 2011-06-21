echo "==Maltese->Hebrew==========================";
bash mt-he.inconsistency.sh > /tmp/mt-he.testvoc; sh inconsistency-summary.sh /tmp/mt-he.testvoc mt-he
echo ""
