#!/usr/bin/env python

import os

param = 0
while True:
    param += 1
    pid = os.fork()
    if pid == 0:
        # need two python first arg is always program name
        os.execlp('python', 'python', 'child.py', str(param))
        assert False, 'error start program'
    else:
        print 'Child is ', pid
        if raw_input() == 'q':
            break
