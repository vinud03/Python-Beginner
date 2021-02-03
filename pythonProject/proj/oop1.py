class student:
    No__of_leaves=9


vinayak=student()
kunal=student()


vinayak.name='Vinayak'
vinayak.roll_no= 5
vinayak.std=16
vinayak.Branch= 'Extc'
print(vinayak.__dict__)

kunal.name='Kunal'
kunal.roll_no=8
kunal.std=16
kunal.Branch='Extc'
print(kunal.__dict__)

print(kunal.Branch)
print(vinayak.Branch)
vinayak.No__of_leaves=17        #create instace variable no_of_leaves for vinayak in its dictionary.
                                # Which will not affect the class variable No_of_leaves
print(vinayak.No__of_leaves)
print(vinayak.__dict__)         #Showing the created instance variable
print(student.No__of_leaves)
student.No__of_leaves=15        #Change the value of the No_of_leaves of class variable
print(student.No__of_leaves)
print(student.__dict__)
