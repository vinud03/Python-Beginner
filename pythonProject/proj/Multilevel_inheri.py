# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def sum(self):
#         return a+b
#
# class B(A):
#     def mul(self):
#         return a*b
#
# class C(B):
#     def division(self):
#         return a/b
#
#
# a=int(input('Enter a number'))
# b=int(input('Enter a number'))
# math=C(a,b)
#
# inp=int(input('press following'
#       '1=+\n'
#       '2=*\n'
#       '3=/'))
# if inp==1:
#     print(math.sum())
# elif inp==2:
#     print(math.mul())
# elif inp==3:
#     print(math.division())
# else:
#     print('Enter a valid input')
#
#
class electronic:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def Elec_devive(self):
        return f'{self.name} is a Electronics device of\n {self.type} type\n'

class pocket_device(electronic):
    category='Pocket device'
    def pocket(self):
        return f'{self.name} is an Electronics device.\nWhich is belong to {self.category} category.\n'\
               f'Which is {self.type} type\n'

class mob(pocket_device):
    category = 'Mobile divice'

    def mobile(self):
        return f'{self.name} is an Electronics device.\nWhich is belong to {self.category} category.\n' \
               f'Which is {self.type} type\n ' \

Printer=electronic('Epson','Wireless')
Earphone=pocket_device('Boat','Wired')
Cellphone=mob('Micromax','Portable')

print(Printer.Elec_devive())
print(Earphone.pocket())
print(Cellphone.mobile())
