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

vinayak=Emp('vinayak',70000,'graduate trainee')
kunal=Emp('Kunal',45000,'Trainee')

print(vinayak.no_of_leaves)

vinayak.change_leaves(14)    #Change class variable(no_of_leaves) using class method

print(Emp.no_of_leaves)