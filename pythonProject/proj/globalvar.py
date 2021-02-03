'''l=50  # global variable. it is not in any function it is at start to function
def func1():
    global l  # After using global function u can change the value of variable
    l=l+15   #can't change the global variable so to change the global variable use global function
    m=2
    print(m,l)


func1()'''

#nested function global variable

x=89
def gana():
    x=20        #local variable x
    def sayali():
        global x
        x=88    #change the global variable
    print("before calling sayali",x)    #printing x dealing with local variable here
    sayali()
    print('after calling sayali',x)     #printing x dealing with local variable here



gana()
print(x)        #printing x dealing with global variable