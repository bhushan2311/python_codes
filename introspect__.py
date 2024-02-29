import inspect

class Employee():
    def __init__(self,name,job):
        self.name=name
        self.job=job
        pass

    def local_var(self,a,b):
        return a,b

    # def __str__(self):
    #     return str(inspect.getmembers(self))

    @classmethod
    def __str__(cls):
        return str(inspect.getmembers(cls))
    pass

emp=Employee("John","Wrestler")
s="uigky"
# print(emp.local_var(2,3))
# print(type(emp))
# print(dir(emp))
# print(inspect.getmembers(emp))
# print(id(s))
print(emp)