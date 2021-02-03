class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A constructor"
        self.classvar1="I am Now instance variable in class A"
        self.special="Special one"


class B(A):
    classvar2="I am class variable in class b"
    def __init__(self):

        self.var1="I am inside class B constructor"
        self.classvar1="I am Now instance variable in class B"
        super().__init__()
        # print(super().fun2)


a=A()
b=B()

print(b.classvar1)
print(b.special)