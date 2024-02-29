# A single class is derived from more than one class

class Employee():
    a=1
    def __init__(self,namee,sal,rol):
        self.name=namee
        self.salary=sal
        self.role=rol

    def addEmp(self,a,b):
        return a+b

class Player():
    a=2
    def __init__(self,namee,gamee):
        self.name=namee
        self.game=gamee

    def subPlay(self,c,d):
        return c+d

# class Person(Employee,Player):   # Sequence is important. Priority is given to that class which comes first in sequence
class Person(Player,Employee):           # player class have priority to getexecute first
    a=3
    """def forEmployee(self):                   # if employee put first in sequence
        print(f"The name is {self.name}, Salary is {self.salary} and the role is {self.role}")"""

    def forPlayer(self):
        print(f"The name is {self.name} & the game is {self.game}")


"""# If Employee comes first in sequence then person takes Employee class constructor arguments  
anil=Employee("ANIL",6555,"Programmer")
# anil=Person("Bhushan","cricket")          #this throws error bcz it takes employee args but provided player class args"""
#anil.forEmployee()

# If Player comes first in sequence then person takes Player class constructor arguments
anil=Person("bhushan","cricket")
# anil=Employee("ANIL",6555,"Programmer")      #this throws error bcz it takes Player args but provided Employee class args"""

anil.forPlayer()
# if there is no 'a' in subclass then that 'a' will print which comes first in sequence
print(anil.a)         # print subclass 'a' as it present in subclass

# just called Super classes methods by sub class instance
print(anil.addEmp(5,6))
print(anil.subPlay(3,2))