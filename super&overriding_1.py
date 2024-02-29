# For OVERRIDDEN default constructor

class Aa():
    a1=4
    def __init__(self):
        self.a1=99
        self.var1="I am inside constructor of class Aa"
        self.special="Special"
        self.hero="hero"

    def __int__(self,a1):         # parametrised constructor
        self.a1=a1
        print(self.a1)

class Bb(Aa):
    a1=5
    var1="d"
    def __init__(self):                     # overriden constructor
        self.a1=23
        self.var1="I am inside constructor of Class Bb"

        # here super() requires, as constructor gets overridden so the variables inside super class const. destroyed and
        # they cant call by sub class instance in order to print those variables we use super
        super().__init__()

        print(super().a1)     # for printing attribute of subclass

        super().__int__(11)


a=Aa()
b=Bb()

print(b.var1)
print(b.a1)
# this will get print iff there is super() or there is no overridden constructor in subclass of super class
print(b.special)           # this will throws error if there is no super