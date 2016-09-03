#!/usr/bin/python
# -*- coding: UTF-8 -*-


import threading
import thread
import os
import time
from threading import Timer


timer_interval = 1

def timer_fun():
    while True:
        time.sleep(0.1)
        print threading.currentThread().name + ' running'
        print 'activeCount=' + str(threading.activeCount())

timer1 = Timer(timer_interval, timer_fun)
timer2 = Timer(timer_interval, timer_fun)

timer1.start()
timer2.start()

while True:
    time.sleep(0.1)
    print threading.currentThread().name + ' running'
    print 'activeCount=' + str(threading.activeCount())