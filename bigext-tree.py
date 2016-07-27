#!/usr/bin/env python

import os, pprint
from sys import argv, exc_info

trace = 1

dirname, extname = os.curdir, '.py'

if len(argv) > 1: dirname = argv[1]
if len(argv) > 2: extname = argv[2]
if len(argv) > 3: trace = int(argv[3])

def tryprint(arg):
    try:
        print unicode(arg)
    except UnicodeEncodeError:
        print arg

visited = set()
allsizes = []

for (root, folders, files) in os.walk(dirname):
    if trace: tryprint(root)
    root = os.path.normpath(root)
    fixname = os.path.normcase(root)
    if fixname in visited:
        if trace: tryprint('skipping', + root)
    else:
        visited.add(fixname)
        for filename in files:
            if filename.endswith(extname):
                if trace > 1: tryprint('+++' + filename)
                fullname = os.path.join(root, filename)
                try:
                    bytes = os.path.getsize(fullname)
                    with open(fullname, 'r') as o:
                        lines = sum(1 for line in o)
                except Exception:
                    print 'error', exc_info()
                else:
                    allsizes.append((bytes, lines, filename))

for (title, key) in [('bytes', 0), ('lines', 1)]:
    print 'By %s...' % title
    allsizes.sort(key=lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])




