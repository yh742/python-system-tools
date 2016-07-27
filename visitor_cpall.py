#!/usr/bin/env python

import os
from visitor import FileVisitor

maxfileload = 1000000
blksize = 1024 * 50

def copyfile(pathFrom, pathTo, maxfileload=maxfileload):
    if os.path.getsize(pathFrom) <= maxfileload:
        bytesFrom = open(pathFrom, 'rb').read()
        open(pathTo, 'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom, 'rb')
        fileTo = open(pathTo, 'wb')
        while True:
            chunk = fileFrom.read(blksize)
            if not chunk: break
            fileTo.write(chunk)

class CpallVisitor(FileVisitor):

    def __init__(self, fromDir, toDir, trace=True):
        self.fromDirLen = len(fromDir)
        self.toDir = toDir
        FileVisitor.__init__(self, trace=trace)

    def visitdir(self, dirpath):
        toPath = os.path.join(self.toDir, dirpath[self.fromDirLen:])
        if self.trace: print 'd', dirpath, '=>', toPath
        os.mkdir(toPath)
        self.dcount += 1

    def visitfile(self, filepath):
        toPath = os.path.join(self.toDir, filepath[self.fromDirLen:])
        if self.trace: print 'f', filepath, '=>', toPath
        copyfile(filepath, toPath)
        self.fcount += 1


if __name__ == '__main__':
    import sys, time
    fromDir, toDir = sys.argv[1:3]
    trace = len(sys.argv) > 3
    print 'Copying ...'
    start = time.clock()
    walker = CpallVisitor(fromDir, toDir, trace)
    walker.run(startDir=fromDir)
    print 'Copied', walker.fcount, 'files', walker.dcount, 'directories',
    print 'in', time.clock() - start, 'seconds'
