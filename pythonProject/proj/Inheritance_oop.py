# # Single Inheritance
# class Emp:
#     no_of_leaves=8
#     def __init__(self,aname,asalary,arole):     #-----
#         self.name=aname                         #     |
#         self.salary=asalary                     #     |   This is Constructor
#         self.role=arole                         #-----
#
#     def details(self):
#         return (f"Name is {self.name}.\nSalary = {self.salary}.\nRole is {self.role}.")
#
#     @classmethod
#     def change_leaves(cls,new_leaves):      #class method
#         cls.no_of_leaves=new_leaves
#
#
#     @classmethod
#     def from_str(cls,str):          #here cls= Emp
#         return cls(*str.split('-'))     #*str.split() its like *arg i.e multiple arguments
#                                         # #str.split convert string into list
#     @staticmethod
#     def printing(str):
#         print("Here is the string",str)
#
#
# class programmer(Emp):
#     def __init__(self,aname,asalary,arole,languages):
#         self.name=aname                         #     |
#         self.salary=asalary                     #     |   This is Constructor
#         self.role=arole
#         self.languages=languages
#
#
#     def printpreog(self):
#         return (f"Programmer Name is {self.name}.\nSalary = {self.salary}.\nRole is {self.role}.\nLanguages know {self.languages}")
#
# vinayak=Emp('vinayak',70000,'graduate trainee')
# sayali=Emp.from_str("Sayali-85000-Sales Executive")
#
# shubham=programmer('Shubham',80000,'Jr.Prgorammer',['Python'])
# karan=programmer('karan',150000,'Sr.Programmer',['C','Java','Python'])
#
# print(shubham.printpreog())
# print(karan.printpreog())

# Multiple Inheritance

class Emp:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):     #-----
        self.name=aname                         #     |
        self.salary=asalary                     #     |   This is Constructor
        self.role=arole                         #-----

    def details(self):
        return (f"Name is {self.name}.\nSalary = {self.salary}.\nRole is {self.role}.")

    @classmethod
    def change_leaves(cls,new_leaves):      #class method
        cls.no_of_leaves=new_leaves


    @classmethod
    def from_str(cls,str):          #here cls= Emp
        return cls(*str.split('-'))     #*str.split() its like *arg i.e multiple arguments
                                        # #str.split convert string into list
    @staticmethod
    def printing(str):
        print("Here is the string",str)


class programmer():
    def __init__(self,aname,asalary,arole,languages):
        self.name=aname                         #     |
        self.salary=asalary                     #     |   This is Constructor
        self.role=arole
        self.languages=languages


    def printpreog(self):
        return (f"Programmer Name is {self.name}.\nSalary = {self.salary}.\nRole is {self.role}.\nLanguages know {self.languages}")

class player(Emp,programmer):
    no_of_games=8
    def pritingdetails(self):
        return (f"name is {self.name}\n can play {self.game}")


vinayak=Emp('vinayak',70000,'graduate trainee')
sayali=Emp.from_str("Sayali-85000-Sales Executive")

shubham=programmer('Shubham',80000,'Jr.Prgorammer',['Python'])
karan=player('karan',150000,'Sr.Programmer')

# print(shubham.printpreog())
print(karan.details())