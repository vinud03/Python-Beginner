# # # ------------- mapfunction-------------------
#
# numbers = ['10','20','5','7']
#
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
#
# print(numbers)
#
# print('Using map function')
# numbers=list(map(int,numbers))
#
# print(numbers)
#
# k=list(map(lambda x:x*x,numbers))
# print(k)
# num=[2,4,8,7,16,5]
# print(num)
# square=list(map(lambda x:x*x , num))
# print(square)
#
#
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# num=[2,4,8,7,16,5]
# func=[square,cube]
# for i in num:
#     val=list(map(lambda x:x(i),func))
#     print(val)
#
# # # ------------- Filter function-------------------
#
# def is_greater_5(num):
#     return num>=5
#
#
# list1=[1,5,7,3,4,6,8]
# gr_5=list(filter(is_greater_5,list1))    #filter bthe list using filter number and again typecast into list using list function
# gr_5.sort()   #sort using sort function
# print(gr_5)
#
#
#
# # # ------------- Reduce function-------------------
# from functools import reduce
#
# l1=[1,5,4,7,8,63,8]
#
# num= reduce(lambda x,y:x+y,l1)
#
# print(num)