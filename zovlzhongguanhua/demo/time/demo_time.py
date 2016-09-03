#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time
from time import struct_time


print '------------------------------------------------------------------------'
print "timezone=" + str(time.timezone)
print "altzone=" + str(time.altzone)
print "daylight=" + str(time.daylight)
print "tzname=" + str(time.tzname)

print '------------------------------------------------------------------------'
print "time=" + str(time.time())
print "clock=" + str(time.clock())

print '------------------------------------------------------------------------'
gm = time.gmtime(1 * 1000 * 1000)
local = time.localtime(1 * 1000 * 1000)

print "gmtime=" + str(gm)
print "localtime=" + str(local)

print '------------------------------------------------------------------------'
print "asctime=" + str(time.asctime((2016, 06, 25, 22, 20,10, 0, 0, 0)))
print "ctime=" + str(time.ctime(1 * 1000 * 1000))

print '------------------------------------------------------------------------'
print "mktime=" + str(time.mktime((2016, 06, 25, 22, 20,10, 0, 0, 0)))