#!/usr/bin/env python

import os, glob, sys, subprocess

dirname = ''

if len (sys.argv) == 1:
    pipes = subprocess.Popen('which python', shell= True, stdout=subprocess.PIPE)
    output = pipes.communicate()
    if not pipes.returncode == 0:
        print 'Cannot find Python on this system'
        sys.exit()
    dirname = os.path.split(output[0].rstrip())[0]
else:
    if not os.path.isdir(sys.argv[1]):
        sys.exit()
    dirname = sys.argv[1]

print 'Searching Directory: %s' % dirname
allsize = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsize.append((filesize, filename))

allsize.sort()
print allsize[:2]
print allsize[-2:]