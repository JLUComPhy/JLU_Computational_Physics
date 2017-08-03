state = 1
ub=1024
lb=0
count=0
import random
n=random.randint(0,1024)

	global state
	global ub
	global lb
	if n_guess == n:
		state = 0
	elif n_guess >0 and n_guess<n:
		ub = ub
		lb = lb + (ub - lb)/2
	elif n_guess >n and n_guess<1024:
		ub = ub - (ub - lb)/2
		lb = lb
		
	
def judge_random(n):
	global state
	global ub
	global lb
	global count
	for index in range(0,10):
		n_guess = (ub + lb)/2
		judge_number(n_guess,n) 
		if state == 0:
			count = count + 1
			break
		elif index == 9:
			break

sample_number=int(input('input sample number:'))
for i in range(0,sample_number):
	judge_random(n)

ratio = count / float(sample_number)		
print(ratio)	
