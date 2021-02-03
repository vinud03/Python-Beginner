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
        # para=str.split('-')         #str.split() split the string in list
        # print(para)
        # return cls(para[0],para[1],para[2])     #we can use 'Emp' instead of 'cls'

        #we can also wite it in one line
        return cls(*str.split('-'))     #*str.split() its like *arg i.e multiple arguments
                                        # #str.split convert string into list
    @staticmethod
    def printing(str):
        print("Here is the string",str)

    def __add__(self,other):                    #This is known as dumder method OR operator overloading
        return self.salary+other.salary         #This method is used to overload on operator add ('+')

    def __truediv__(self, other):               #overload / operator
        return self.salary/other.salary


emp1=Emp('Vinayak',750,"graduate trainee")
emp2=Emp('Kunal',250,'Youtuber')

print(emp1+emp2)
print(emp1/emp2)