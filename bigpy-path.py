#!/usr/bin/env python

import sys, os, pprint
trace = 0

visited = {}
allsizes = []

for srcdir in sys.path:
    for (root, folder, files) in os.walk(srcdir):
        if trace > 0: print root
        root = os.path.normpath(root)
        fixcase = os.path.normpath(root)
        if fixcase in visited: continue
        else:
            visited[fixcase] = True
        for filename in files:
            if filename.endswith('py'):
                if trace > 1: print '...', filename
                pypath = os.path.join(root, filename)
                try:
                    pysize = os.path.getsize(pypath)
                except os.error:
                    print 'skipping', pypath, sys.exc_info()[0]
                else:
                    pylines = len(open(pypath, 'r').readlines())
                    allsizes.append((pysize, pylines, pypath))

print 'By size...'
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])