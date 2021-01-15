
import RAnd_num



def guess():
'''
This function is created to generate one random number.
Here we take input from user and compare it with random number

'''
    num = RAnd_num.randint(1, 15)
    print("Guess the number from 1 to 15\n Total number of attempts 5")
    print('Enter the Number you guess')
    for i in range(1, 6):
        num2 = int(input())
        if num2 > num:
            print('Enter number is greater\n Try again')
        elif num2 < num:
            print('Enter number is smaller\n Try again')
        elif num2 == num and i <= 5:
            print('Congratulation you guess correctly in %d attempt' % i)
            break
        elif (i == 5 and num2 != num):
            print("The correct answer is:%d" % num)
        else:
            print('Guess again\n %d attempt left' % (5 - i))
        i = i + 1




while(True):
    guess()
    print("Press Y to play again\nOR\nPress any key ")
    k=input()
    if k=='Y' or k=='y':
        guess()
    else:
        break
