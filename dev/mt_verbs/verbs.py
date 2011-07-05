#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy, time;
import classes;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
reload(sys); sys.setdefaultencoding("utf-8")

STEMSFILE=sys.path[0] + '/stems.csv';
FORMAT="speling"

if len(sys.argv)>0:
    if '--help' in sys.argv:
        print "Usage: verbs.py [-F file] [-s \"stem line\"] [--dix]"
        sys.exit(1)

    if '--dix' in sys.argv:
        FORMAT="dix"
    
    if '-F' in sys.argv:
        fi = sys.argv.index('-F')
        if len(sys.argv)>fi+1:
            STEMSFILE=sys.argv[fi+1]
        else:
            sys.stderr.write("Error: no file specified\n")
            sys.exit(1)

    if '-s' in sys.argv:
        si = sys.argv.index('-s')
        if len(sys.argv)>si+1:
            STEMSFILE = False
            lines = [sys.argv[si+1]]
        else:
            sys.stderr.write("Error: no stem line specified\n")
            sys.exit(1)

if STEMSFILE:
    try:
        lines = file(STEMSFILE)
    except IOError as e:
        sys.stderr.write("Error reading file: {0}\n".format(STEMSFILE))
        sys.exit(1)

def format_entry(FORMAT, stem, form, pos, feat):
    if FORMAT=="speling":
        return stem + '; ' + speling[feat] + '; ' + feat + '; ' + pos;
    elif FORMAT=="dix":
        tags = ''.join(['<s n="%s"/>' % tag
                for tag in [pos] + feat.split('.')])
        tags = tags.replace('<s n="+neg"/>', '<j/>x<s n="neg"/>'); # TODO: what should the negative lemma be?
        tags = tags.replace('<s n="+probj"/>', '<j/>prpers<s n="prn"/><s n="obj"/>')
        return "    <e><p><l>%s</l>\t<r>%s%s</r></p></e>" % (speling[feat],
                                     stem,
                                     tags);
    else:
        raise(Exception);

if FORMAT=="dix": 
    print '  <section id="verbs" type="standard">';
    print '    <!-- Generated on: ' + time.strftime('%Y-%m-%d %H:%M %Z') + ' -->'; 


for line in lines:
    if len(line) < 2 or line[0] == '#':
        continue
    
    row = line.split(',')
    
    #stem, category, gloss, root, vowels, subclass, checked
    stem = row[0].strip()
    category = row[1].strip()
    root = row[3].strip().split('-')
    vowels = row[4].strip().split('-')
    subclass = row[5].strip() if (len(row) >= 5) else None
    pos = 'vaux' if category == 'vaux' else 'vblex'
    
    # build class name
    classname = category
    if subclass:
        classname = classname + '_' + subclass

    try:
        klass = getattr(classes, classname)
        speling = klass.main(stem, root, vowels)
        feats = [f for f in speling.keys() if speling[f]]
        feats.sort()    # pretty
        for feat in feats:
            print format_entry(FORMAT, stem, speling[feat], pos, feat);
            
    except AttributeError:
        sys.stderr.write("Error: Missing class '{0}'".format(classname))
        
    print '' # newline between words


if FORMAT=="dix": print '  </section>';
