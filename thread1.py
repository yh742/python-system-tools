#!/usr/bin/env python
import thread


def child(tid):
    print 'Hello from thread', tid


def action(i):
    print i ** 32


class Power:
    def __init__(self, i):
        self.i = i

    def action(self):
        print self.i ** 32


def parent():
    i = 0
    while True:
        i += 1
        thread.start_new_thread(child, (i,))
        if raw_input() == 'q':
            break

thread.start_new_thread(action, (2,))

thread.start_new_thread((lambda: action(2)), ())

obj = Power(2)
thread.start_new_thread(obj.action, ())

