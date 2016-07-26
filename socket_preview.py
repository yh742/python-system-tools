#!/usr/bin/env python

import socket

port = 50008
host = 'localhost'

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = 'server got: [%s]' % data
        conn.send(reply)

def client(name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name)
    reply = sock.recv(1024)
    sock.close()
    print 'client got: [%s]' % reply


if __name__ == '__main__':
    from threading import Thread
    sthread = Thread(target=server)
    sthread.daemon = True
    sthread.start()
    for i in range(5):
        Thread(target=client, args=('client %s' % i,)).start()
