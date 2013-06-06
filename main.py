#!/usr/bin/env/python
from spartacus import Spartacus

s = Spartacus()
s.connect()
s.setJointSpeed(1, 180)
s.resetToZero()
myin = raw_input("Device moved to zero. Please affix the lock now. Press a key to continue")
s.stop()
"""
print("Moving to 13...")
s.resetToNumber(13)
print("Moving to 27...")
s.ccwToNumber(13)
s.ccwToNumber(27)
print("Moving to 21...")
s.cwToNumber(21)
"""
s.guess_combos(13)
