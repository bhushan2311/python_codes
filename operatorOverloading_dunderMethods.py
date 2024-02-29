class hopper():

    def __init__(self,a1,b1):
        self.a=a1
        self.b=b1

    def __add__(self, other):                  # dunder methods
        return self.a+other.a,self.b+other.b
    def __truediv__(self, other):
        return self.a/other.a,self.b/other.b

    def __neg__(self):
        return -self.b
    def __mul__(self, other):
         return self.a*other.b

    # def fun(self,w):
    #     return w
    pass

h1=hopper(3,4)
h2=hopper(4,6)

print(h1+h2)               # overloaded + operator to add to objects or added imaginary numbers
print(h1/h2)
print(-h2)
print(h1*h2)
# print(h1.fun(3)+h2.fun(4))




# class harbour():
#     def __init__(self,aname,ajob,asalary):
#         self.name=aname
#         self.job=ajob
#         self.salary=asalary
#
#     def __add__(self, other):
#         return self.name+other.name
#
#     def __repr__(self):
#         return f"The name is {self.name}"
#
#     def __str__(self):      # this has higher priority than __repr__
#         return f"The job is {self.job}"
#
#     pass
#
# ho=harbour("Elizabeth","Actress",2323)
# hos=harbour(" Bhushan Ambhore","Student",34)
# # print(ho)              # this prints __str__ as it has higher priority than __repr__
# print(str(ho),repr(ho))
# print(ho+hos)
