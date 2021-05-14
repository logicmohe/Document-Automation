#!/usr/bin/python
import sys
import time

def tomato_timer():
  # sleep for 25 mins
  # each counter represents 30 seconds
  total, counter = 50, 50
  while counter:
    print('|', end='')
    for i in range(total-counter):
      print('>', end='')
    for i in range(counter):
      print('=', end='')
    
    print('|')
    counter -= 1
    time.sleep(3)

if (len(sys.argv)==1):
  tomato_timer()