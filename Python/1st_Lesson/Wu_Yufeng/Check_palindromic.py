n = input('Please enter a number : ')
n_str = str(n)
n_list = list(n_str)
for i in range(0,len(n_str)/2):
	temp=n_list[i] 
	n_list[i] = n_list[len(n_str)-i-1]
	n_list[len(n_str)-i-1] = temp
	
c_int = int(''.join(n_list))
if n == c_int:
	print(n_str+' is a palindromic number! ')
else:
	print(n_str+' is not a palindromic number! ')
