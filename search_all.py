#!/usr/bin/env python

import os, sys
listonly = False
textexts =  ['.py', '.pyw', '.txt', '.c', '.h']

def searcher(startdir, searchkey):
    global fcount, vcount
    fcount = vcount = 0
    for (root, subs, files) in os.walk(startdir):
        for fname in files:
            fpath = os.path.join(root, fname)
            visitfile(fpath, searchkey)

def visitfile(fpath, searchkey):
    global fcount, vcount
    print vcount + 1, '=>', fpath
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in textexts:
                print 'Skipping', fpath
            elif searchkey in open(fpath).read():
                raw_input ('%s has %s' % (fpath, searchkey))
                fcount += 1
    except:
        print 'Failed:', fpath, sys.exc_info()[0]
    vcount += 1


if __name__ == '__main__':
    searcher(sys.argv[1], sys.argv[2])
    print 'Found in %d files, visited %d' % (fcount, vcount)