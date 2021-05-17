#!/usr/bin/python
import sys
import time

class Timer():
  PERIOD = 30
  def __init__(self):
    pass
  def tomato_on(self):
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

  def tomato_cycle(self):
    # Start from 9:00 to 17:00
    for i in range(17-9):
      self.tomato_on()
      print('Tomato Timer End !!!')

      self.tomato_off()
      print('Time to work!!!')

if (len(sys.argv)==1):
  timer = Timer()
  timer.tomato_cycle()