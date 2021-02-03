n = int(input('Enter a number'))
m=int(input('press 1 if you print pattern in descending order'
            'press 1 if you print pattern in ascending order'))
m=bool(m)
k=n+1
if (m==True):
    for i in range(1,k):
        for j in range (i):
            print('*',end='')

        print()

else:
    for i in range(1, k):
        for j in range(k-i):
            print('*', end='')
        print()