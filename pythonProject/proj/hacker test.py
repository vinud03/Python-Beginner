"""
If  is odd, print Weird
If  is even and in the inclusive range of  to , "print Not Weird"
If  is even and in the inclusive range of  to , "print Weird"
If  is even and greater than , print "Not Weird"
"""
#
# N = int(input())
# if N%2==0:
#     if N>=2 and N<=5:
#          print('Not Weird')
#     elif N>=6 and N<=20:
#         print('Weird')
#     else:
#         print('Not Weird')
# else:
#     print('Weird')


# class Person:
#     def __init__(self, initialAge):
#         # Add some more code to run some checks on initialAge
#         self.age = initialAge
#         if self.age < 0:
#             self.age = 0
#             print('Age is not valid, setting age to 0.')
#
#     def amIOld(self):
#         # Do some computations in here and print out the correct statement to the console
#         if age < 13:
#             print('You are young.')
#         elif 13 <= age < 18:
#             print('You are a teenager.')
#         else:
#             print('You are a old.')
#
#     def yearPasses(self):
#         # Increment the age of the person in here
#         self.age=age+1
#
#
# t = int(input())
# for i in range(0, t):
#     age = int(input())
#     p = Person(age)
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()
#     p.amIOld()
#     print("")


x = int(input())
y = int(input())
z = int(input())
n = int(input())
lp=[]
ls=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if ((i+j+k))!=n:
                lp=[i,j,k]
                ls.append(lp)
print(ls)