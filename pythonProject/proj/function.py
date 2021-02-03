# a=5
# b=7
# print(sum((a,b)))   #built in function


def func1(a,b):
    sum=a+b
    print(sum)

# print(func1(9,5))


def func2(a,b):
    '''This is function which calculate average of the two numbers'''  # This is the doc string of function, which is denoted by ''''''.
    avg=(a+b)//2
    return avg

v=func2(8,5)
print(func2.__doc__)
print(v)