#!/usr/bin/env python3
from spartacus import Spartacus

def main():
    s = Spartacus()
    s.trial_run = True
    s.setJointSpeed(2, 180)
    s.setJointSpeed(1, 180)
    s.reset()
    s.moveJointTo(2, 0)
    myin = input("Device moved to zero. Please affix the lock now. Press enter to continue")
    s.stop()
    """
    for i in range(0,40):
      if s.guess_combos(i):
        break
    """
    s.guess_combos(38)

if __name__ == '__main__':
    main()
