#!/usr/bin/env/python
from spartacus import Spartacus

s = Spartacus()
s.connect()
s.setJointSpeed(2, 180)
s.setJointSpeed(1, 180)
s.reset()
s.moveJointTo(2, 0)
myin = raw_input("Device moved to zero. Please affix the lock now. Press a key to continue")
s.stop()
for i in range(0,40):
  if s.guess_combos(i):
    break
