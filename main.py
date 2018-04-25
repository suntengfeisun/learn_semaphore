# coding:utf8

import threading
from Queue import Queue
from random import randint
from time import sleep


def do_print(t):
    while 1:
        try:
            values = my_queue.get()
            sleep(values[1])
            print('thread_{}'.format(t), values[0])
        except:
            pass


def do_print_new(t):
    while 1:
        try:
            values = my_queue.get()
            sleep(values[1])
            sem.acquire()
            print('thread_{}'.format(t), values[0])
            sem.release()
        except:
            pass


def main():
    for i in xrange(1000):
        my_queue.put((i, randint(0, 1)))
    my_threads = []
    for t in xrange(10):
        # my_threads.append(threading.Thread(target=do_print, args=(t,)))
        my_threads.append(threading.Thread(target=do_print_new, args=(t,)))
    for my_thread in my_threads:
        my_thread.start()
    for my_thread in my_threads:
        my_thread.join()


if __name__ == '__main__':
    my_queue = Queue()
    sem = threading.Semaphore(value=1)
    main()
