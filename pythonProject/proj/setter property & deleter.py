class employee():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property                               #we can use that method without using parenthesis
    def email(self):
        if self.fname==None or self.lname==None:
            return ("Email is not set. Please set it using setter.")
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter                          #can modify(overwrite) the function which is previously defined in same class by assigning value to it
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter                          #Can delete function using this decorator
    def email(self):
        self.fname = None                   #we not delete method n oop we just clear there variables by using "None"
        self.lname = None


gana=employee("Vinayak","Dagade")
sayali=employee("Sayali","Dagade")

print(gana.email)
gana.lname="Lincon"
print(gana.email)


del gana.email
print(gana.email)

gana.email="Vinu.d03@gmail.com"
print(gana.lname)
print(gana.fname)
print(gana.email)