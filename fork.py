#!/usr/bin/env python

import os


def child():
    print 'Hello from child', os.getpid()
    os.exit(0)


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print 'Hello from parent', os.getpid(), newpid
        if raw_input() == 'q':
            break



