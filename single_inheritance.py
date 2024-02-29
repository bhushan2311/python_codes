
class Employee():
    def __init__(self,namee,sal,rol):
        self.name=namee
        self.salary=sal
        self.role=rol

    def add(self,a,b):
        return a+b


class Programmer(Employee):
    def __init__(self,namee,sal,rol,lang):
        self.name=namee                      # bad approach - use instead super 
        self.salary=sal
        self.role=rol
        self.language=lang

    def show(self):
        print(f"The name is {self.name}, salary is {self.salary} and the role is {self.role} and knows {self.language}")

harry=Employee("HARRY",2400,"Instructor")

rohan=Programmer("ROHAN",2300,"Programmer",["java","cpp"])
rohan.show()     # to show, sub class instance can access super class methods
print(rohan.add(3,4))
# harry.show()            # throws error as parent class obj cant access child class methods