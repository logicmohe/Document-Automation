#!/usr/bin/python
import sys
import time

class Timer():
  PERIOD = 30
  def __init__(self):
    pass
  def tomato_on(self, min=25):
    # sleep for 25 mins
    # each counter represents 30 seconds
    total, counter = 50, 50 - min*2
    while counter:
      print('|', end='')
      for i in range(total-counter):
        print('>', end='')
      for i in range(counter):
        print('=', end='')
      print('|')
      counter -= 1
      time.sleep(self.PERIOD)
  def tomato_off(self):
    # sleep for 25 mins
    # each counter represents 30 seconds
    total, counter = 10, 10
    while counter:
      print('Rest Period |', end='')
      for i in range(total-counter):
        print('>', end='')
      for i in range(counter):
        print('=', end='')
      print('|')
      counter -= 1
      time.sleep(self.PERIOD)

  def tomato_cycle(self, c_hr, c_min):
    # Start from 9:00 to 17:00
    period = (17-c_hr)*2
    if c_min >= 30:
      c_min -= 30
      period += 1
    
    for i in range(period):
      self.tomato_on(c_min)
      c_min = 25
      print('Tomato Timer End !!!')
      self.tomato_off()
      print('Time to work!!!')

if (len(sys.argv)==1):
  c_hr = int(time.strftime("%H",time.gmtime()))-4
  c_min = int(time.strftime("%M",time.gmtime()))

  timer = Timer()
  timer.tomato_cycle(c_hr, c_min)