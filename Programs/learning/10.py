print('Enter a Number:')
n=int(input())
if n<10:
	print('{} is less than 10'.format(n))
elif n>10:
	print('{} is greater than 10'.format(n))
else: 
	print('{} is equal to 10'.format(n))