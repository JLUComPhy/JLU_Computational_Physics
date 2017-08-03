import numpy as np
def qe_solution(a,b,c):
  if a == 0:
    x = -c/b
    print('Solution is : '+str(x))
	elif pow(b,2)-4*a*c > 0:
		x1 = (-b + np.sqrt(pow(b,2)-4*a*c))/float(2)
		x2 = (-b - np.sqrt(pow(b,2)-4*a*c))/float(2)
		print('Solutions are :'+str(x1)+'and'+str(x2))
	elif pow(b,2)-4*a*c == 0:
		x = -b/float(2*a)
		print('Solution is : '+str(x))
	else:
		x1 = complex(-b,np.sqrt(-pow(b,2)+4*a*c))/float(2*a)
		x2 = complex(-b,-np.sqrt(-pow(b,2)+4*a*c))/float(2*a)
		print('Solutions are : '+str(x1)+'and'+str(x2))
		
a = float(input('Please input a : '))
b = float(input('Please input b : '))
c = float(input('Please input c : '))
qe_solution(a,b,c)

