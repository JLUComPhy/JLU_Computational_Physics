#!/usr/bin/python2.7
# Find the No.x prime number 

prime_list = [2]
number = 3

print "Please input the index of the prime number you want to find:"
index = int(raw_input('>'))

while len(prime_list) < index:
  for prime_number in prime_list:
    if number % prime_number == 0:
      break
  else:
    prime_list.append(number)
  number += 1

print prime_list[index-1]
  
    
