#!/usr/bin/env/python
from barobo.linkbot import *
import time

class Spartacus(Linkbot):
  def __init__(self):
    self.__current_number = 0
    Linkbot.__init__(self)
    self.combo_guess1 = 0
    self.combo_guess2 = 0
    self.combo_guess3 = 0

#Testing combo: 0, 2, 36
#CW Delta -36 0 36
  def cwToNumber(self, number):
    """Turn the combo-lock dial clockwise to get to the specified dial number.

       If the dial is already at the number, a full rotation is performed."""
    while number >= self.__norm(self.__current_number):
      number -= 40
    delta = -abs(self.__norm(self.__current_number) - number)
    self.__current_number += delta
    if abs(delta) <= 4:
      self.driveJointToNB(1, self.__current_number * -360.0 / 40.0)
      self.__moveWait()
    else:
      self.moveJointToNB(1, self.__current_number * -360.0 / 40.0)
      self.__moveWait()
  
  def ccwToNumber(self, number): 
    """Turn the combo-lock dial counter-clockwise to get to the specified dial number.

       If the dial is already at the number, a full rotation is performed."""
    while number <= self.__norm(self.__current_number):
      number += 40
    delta = abs(self.__norm(self.__current_number) - number)
    self.__current_number += delta
    if abs(delta) <= 4:
      self.driveJointToNB(1, self.__current_number * -360.0 / 40.0)
      self.__moveWait()
    else:
      self.moveJointToNB(1, self.__current_number * -360.0 / 40.0)
      self.__moveWait()

  def resetToNumber(self, number):
    self.cwToNumber(number)
    self.cwToNumber(number)
    self.cwToNumber(number)

  def guess_combos(self, firstnum):
    print "Resetting to first num..."
    self.resetToNumber(firstnum)
    num2range = range(firstnum+2, firstnum + 2 + 40, 4)
    num2range = map( lambda x: x%40, num2range)
    # CCW one full rotation to engage second ring
    print "Engaging second ring..."
    self.ccwToNumber(firstnum)
    for i in num2range:
      print "Moving to second number"
      self.ccwToNumber(i)
      num3range = range(i+2, i+2+40, 4)
      num3range = map( lambda x: x%40, num3range)
      num3range = reversed(num3range)
      for j in num3range:
        print "Testing combo: {0}, {1}, {2}".format(firstnum, i, j)
        self.cwToNumber(j)
        self.setMotorPower(2, 200)
        time.sleep(0.5)
        self.setMotorPower(2, -200)
        time.sleep(0.5)
        self.setMotorPower(2, 0)
      print "Moving back to second ring..."
      self.ccwToNumber(i)


  def __norm(self, num):
    while num < 0:
      num += 40
    while num >= 40:
      num -= 40
    return num

  def __moveWait(self):
    [j1, _, _] = self.getJointAngles()
    j1 = j1 * -40.0 / 360.0
    while abs( j1 - self.__current_number) > 0.5:
      [j1, _, _] = self.getJointAngles()
      j1 = j1 * -40.0 / 360.0

