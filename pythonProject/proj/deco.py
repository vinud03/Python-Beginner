def dec1(func1):
    def nowexec():
        print('Executing now')
        func1()
        print('Executed')
    return nowexec
# @dec1
def who_is_vinayak():
    print('Vinayak is good boy')


who_is_vinayak=dec1(who_is_vinayak)

who_is_vinayak()