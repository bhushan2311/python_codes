# For OVERRIDDEN methods

class AA():
    q="AA attribute"
    def fun(self):
        self.q="AA method"
        print("this is method of class AA")
    pass

class Bb(AA):
    q="Bb attribute"
    def fun(self):        # Overriden
        self.q="Bb method"
        print(self.q)
        print("this is method of class Bb")
        super().fun()
        print(super().q)

    # def fun2(self,a):
    #     print(a+1)
    pass

a=AA()
b=Bb()

print(b.q)
b.fun()
# b.fun2(3)