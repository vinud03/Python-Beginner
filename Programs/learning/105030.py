print('Enter a Number:')
n=int(input())
if n%10==0 and n%50==0:
	if n%30==0:
		print('{} is divisible by 10,50,30'.format(n))
	else:
		print('{} is divisible by 10 and 50 but not 30' .format(n))