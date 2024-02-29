
class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary

    @classmethod
    def leaves(cls,new_leaves): # if there is (self) and no decorator then no_of_leave will only change for that instance which calling this method
        cls.no_of_leaves=new_leaves # this changes class's no_of_leaves when any of instance call this method & and it will share by all instances


harry=Employee("Harry",2300)
rohan=Employee("Rohan",2000)

print(rohan.no_of_leaves)         # o/p : 8
# harry.no_of_leaves=90
harry.leaves(78)            # this changes the class's no of leaves bcz of classmethod decorator

print(harry.no_of_leaves)      # o/p : 78

print(rohan.no_of_leaves)      # o/p : 78