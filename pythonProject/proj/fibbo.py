# def fibbo_iterative(n):
#     """Using iterative methode"""
#     n1=0
#     n2=1
#     print(n1,n2,end=',')
#     j=0
#     for i in range(n):
#         j=n1+n2
#         n1=n2
#         n2=j
#         print(n2,end=',')
#
# print(fibbo_iterative.__doc__)
# n=int(input('Enter the number upto fibbonacci series print'))
# fibbo_iterative(n)
#


def fibo_recursive(n):
    ''' recursive method of fibonacci series'''
    if n<=1:
        return n
    else:
        return(fibo_recursive(n-1)+fibo_recursive(n-2))


print(fibo_recursive.__doc__)
n=int(input('Enter number of element'))
for i in range (n):
    print(fibo_recursive(i),end=',')
