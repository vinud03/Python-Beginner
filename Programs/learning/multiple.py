print("Enter a Number")
n =int(input())
if n%3 == 0:
    print("Number is multiple of 3")
    if n%7==0:
        print("Number is multiple of 7")
    else:
        print("Number is multiple of 3 but not multiple of 7")
