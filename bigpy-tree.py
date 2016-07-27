#!/usr/bin/env python

import sys, os, pprint

trace = False

if sys.platform.startswith('win'):
    dirname = r'C:\Python27'
else:
    dirname = '/usr/lib/python2.7'

allsizes = []
for (root, dir, files) in os.walk(dirname):
    if trace:
        print root
    for filename in files:
        if filename.endswith("py"):
            if trace:
                print '...', filename
            fullname = os.path.join(root, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])