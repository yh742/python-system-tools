#!/usr/bin/env python

import thread, time

numthreads = 5
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

def counter(myId, count, mutex):
    with mutex:
        for i in range(count):
            time.sleep(1 / (myId + 1))
            print '[%s] => %s' % (myId, i)
    exitmutexes[myId].acquire()

for i in range(numthreads):
    thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25)
print 'Main thread exiting.'

