# 43*3=555; 56+9=77;    56/6=4

X=1
while(X==1):
    num1 = int(input('Enter first Number'))
    operator = input('Operation you have to perform')
    num2 = int(input('Enter second number'))
    if(num1==43 and num2==3 and operator=='*'):
        print(555)
    elif(num1==56 and num2==9 and operator=='+'):
        print(77)
    elif(num1==56 and num2==6 and operator=='/'):
        print(4)
    elif(operator=='+'):
        print(num1+num2)
    elif(operator=='-'):
        print(num1 - num2)
    elif(operator=='*'):
        print(num1*num2)
    elif(operator=='/'):
        print(num1/num2)
    print('You want to calculate again?\n  Y or N ')
    x=input()
    if x=='Y' or x=='y':
        X=1
    else:
        X=0