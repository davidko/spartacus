#!/usr/bin/env/python
from spartacus import Spartacus

s = Spartacus()
s.connect()
s.setJointSpeed(2, 180)
s.setJointSpeed(1, 180)
s.resetToZero()
myin = raw_input("Device moved to zero. Please affix the lock now. Press a key to continue")
s.stop()
print("Moving to 0...")
s.resetToNumber(0)
print("Moving to 18...")
s.ccwToNumber(0)
s.ccwToNumber(18)
print("Moving to 8...")
s.cwToNumber(8)
print s.checkShackle()
"""
s.guess_combos(13)
"""
