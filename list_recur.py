#!/usr/bin/env python
import sys, os


def mylister(currdir):
    print('[%s]' % currdir)
    for file in os.listdir(currdir):
        path = os.path.join(currdir + file)
        if os.path.isdir(path):
            mylister(path)
        else:
            print path


if __name__ == "__main__":
    mylister(sys.argv[1])
