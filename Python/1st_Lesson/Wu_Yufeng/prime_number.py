# -*- coding: utf-8 -*-
import numpy as np
#定义判断函数
def identify_prime(n):
	global state
	state = 0
	if n == 2 :	
		state =0
	else:
		check_max=int(np.sqrt(n)+1)
		for i in range(2,check_max):
		  if n%i == 0:
			  state = 1
			  break
		
a = input('which prime : ')
count = 0
check_max = int(pow(a,2))
for i in range(2,check_max):
	if count == a:
		print('The '+str(a)+'th prime number is : '+str(i-1))
		break 
	else:
		identify_prime(i)
		if state == 0:
			count = count + 1
		
