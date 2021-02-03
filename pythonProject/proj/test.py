# import cmath
#
# def quadratic_Eq():
#
#     '''function to solve quadratic equation'''
#     a = float(input('Enter a: '))
#     b = float(input('Enter b: '))
#     c = float(input('Enter c: '))
#     # calculate the discriminant
#     d = (b ** 2) - (4 * a * c)
#
#     # find two solutions
#     sol1 = (-b - cmath.sqrt(d)) / (2 * a)
#     sol2 = (-b + cmath.sqrt(d)) / (2 * a)
#     print('The solution are {0} and {1}'.format(sol1, sol2))
#
#
# def swap_two_num():
#     '''function to swap two numbers'''
#     a=int(input('Enter a number:'))
#     b=int(input('Enter a number:'))
#     print(a,b)
#     a=a+b
#     b=a-b
#     a=a-b
#     print(a,b)

    # n=int(input('Enter a number:'))
    # if n%2==0:
    #     print("{} is even number".format(n))
    # elif n%2!=0:
    #     print("{} is odd number".format(n))
    #



#Find the year is leap year or not
# year = int(input("Enter a year: "))
# if (year % 4) == 0:
#     # print(year%4)
#     if (year % 100) == 0:
#        print(year%100)
#        if (year % 400) == 0:
#            print(year%400)
#            print("{0} is a leap year".format(year))
#        else:
#            print("{0} is not a leap year".format(year))
#     else:
#         print("{0} is a leap year".format(year))
# else:
#    print("{0} is not a leap year".format(year))



# check whether given number is prime or not
# num = int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")


# def fact(n):
#     if n<=1:
#         return 1
#     return (n*fact(n-1))
#
# n=int(input('Enter a number'))
# print(fact(n))


# printing start pattern
# x='*'
# n=int(input('Enter range of the pattern'))
# for i in range (1,n+1):
#     for j in range(i):
#         print(x, end='')
#     print('\n')



#check amstrong number
n=int(input('Enter a range'))
for i in range (n):
    k=i
    sum=0
    x=0
    while(k>0):
        t=k%10
        sum=sum+(t**3)
        k=k//10
    if sum==i:
        print('{} is an armstrong number'.format(sum))
    # else:
    #     print('{} is not an armstrong number'.format(sum))
