
class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def s(self):
        pass

    @classmethod
    def comma(cls,string):
        # a=string.split(",")
        # print(a)            # will print list
        # return cls(a[0],a[1],a[2])
        return cls(*string.split(","))  # (returns object) this return cls() is for constructor ie. the arguments here get receive by constructor arguments

    @classmethod
    def ab(cls,str1,str2,str3):         # dummy method just to show how above decorator working
        return cls(str1,str2,str3)      # (returns object)


karan=Employee("KARAN",2100,"imposter")
# print(karan.name)
# print(karan.salary)
# print(karan.role)

arjun=Employee.comma("ARJUN,1200,warden")
print(arjun.name)

Ab=Employee.ab("ADITYA",44,"worker")
print(Ab.name)

karan.s()