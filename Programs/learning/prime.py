print('Enter a number:')
n=int(input())
k=n//2
for i in range(2,n):
	if n%i==0:
		print('Number is not prime number')
		break
else:
	print('Number is prime number')