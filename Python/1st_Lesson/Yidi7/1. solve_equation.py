#!/usr/bin/python2.7
# Solve quadratic equation

from cmath import sqrt
print "Please input the coefficient of the equation: ax^2 + bx + c = 0"
a = float(raw_input("a = ? "))
b = float(raw_input("b = ? "))
c = float(raw_input("c = ? "))

if a == 0:
  x = -c/b
  print "x = %s" % x
else:
  x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
  x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
  print "x1 = %s, x2 = %s" % (x1, x2)

  
