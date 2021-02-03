class A:
    classvar1="I am s class variable of class A"
    def __init__(self):
        self.var1="I am inside class A constructor"
        self.classvar1='I am now instance var of class A'
        self.special="Special variable"

class B(A):
    classvar1="I am a class variable of class B"
    # def __init__(self):
    #     self.var1="I am inside class B constructor"
    #     self.classvar1="I am instance variable of class B"
    # pass

a=A()
b=B()

print(a.var1)
print(b.var1)
print(a.special)
# print(b.special)            #HEre the constructor of class A is get overwrite in class B so we cannot acess class A's
                            # constructor using class B

print(b.classvar1)