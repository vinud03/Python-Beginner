def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


n=int(input('Enter a number'))
print('factorial using recursive approach\n',factorial(n))

print("Iterative approach for factorial")
fac=1
for i in range (n):
    fac=(i+1)*fac

print(fac)