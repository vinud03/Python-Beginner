class Emp:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):     #-----
        self.name=aname                         #     |
        self.salary=asalary                     #     |   This is Constructor
        self.role=arole                         #-----

    def details(self):
        return (f"Name is {self.name}.\nSalary = {self.salary}.\nRole is {self.role}.")


vinayak=Emp('vinayak',70000,'graduate trainee')
kunal=Emp('Kunal',45000,'Trainee')

# vinayak.name='Vinayak'
# vinayak.salary=7855
# vinayak.role='Trainee'
# print(Emp.details(vinayak))   #both work similar
print(vinayak.details())

print('\n')
# kunal.name='Kunal'
# kunal.salary=7844
# kunal.role='Trainee'
print(kunal.details())