#!/usr/bin/python2.7
#
# 998049884 right guesses out of 1000000000, percent: 0.998049884
# 0 and 1024 cannot be reached, 2/1025 = 0.00195122

import random

def guess_number_manually():
  x = random.randint(0, 1024)
  for i in range(10):
    print "Guess an integer from 0 to 1024: %s time(s) left" % (10 - i)
    x_guess = int(raw_input('>'))
    if x == x_guess:
      return "Congrats! x is %s" % x    
    if x > x_guess:
      print "x is greater than your guess"
    elif x < x_guess:
      print "x is less than your guess"
  else:
    return "Sorry but you have run out of guesses. x is %s" % x
    
def guess_number_automatically(ntimes):
  right_times = 0
  i = 0
  while i < ntimes:
    x = random.randint(0, 1024)
    lower_bound = 0
    upper_bound = 1024
    x_guess = 512
    for j in range(10):
      if x == x_guess:
        right_times += 1
        break
      if x > x_guess:
        lower_bound = x_guess
      elif x < x_guess:
        upper_bound = x_guess
      x_guess = (lower_bound + upper_bound)/2
    i += 1
  return right_times
      

if __name__ == "__main__":
  print ("Do you want guess the number manually or automatically? "
          "manually = 1; automatically = 2")
  mode = int(raw_input('>'))
  if mode == 1:
    print guess_number_manually()
  elif mode == 2:
    print "How many times do you want to loop?"
    ntimes = int(raw_input('>'))
    right_times = guess_number_automatically(ntimes)
    right_percent = float(right_times)/float(ntimes)
    print "%s right guesses out of %s, percent: %s" % (right_times, ntimes, right_percent)
  else:
    print "Error, please input 1 or 2"

    
