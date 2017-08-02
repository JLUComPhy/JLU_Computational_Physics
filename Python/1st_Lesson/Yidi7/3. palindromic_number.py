#!/usr/bin/python2.7
# Figure out if a number is palindromic or not 

print "please input an integer:"
number = raw_input('>')
length = len(number)

for i in range(length/2):
  if number[i] != number[length-1-i]:
    print "%s is not a palindromic number" % number
    break
else:
  print "%s is a palindromic number" % number

  
