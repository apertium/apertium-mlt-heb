#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, re;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
reload(sys); sys.setdefaultencoding("utf-8")

if len(sys.argv)<2:
    print "Usage: mark_analysed.py <freqlist>"
    sys.exit(1)

try:
    lines = file(sys.argv[1])
except IOError as e:
    sys.stderr.write("Error reading file {0}\n".format(sys.argv[1]))
    sys.exit(1)

# go over freqlist and check analyse
p = re.compile('\^.*\/\*(.*)\$')
for line in lines:
    match = p.match(line.strip())
    key = match.group(1).lower() if match else None
    print key

    if key:
        print "+" + key
    else:
        sys.stdout.write(line)
