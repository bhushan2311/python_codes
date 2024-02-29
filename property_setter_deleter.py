
class Employee():
    def __init__(self,name,job):
        self.name=name
        self.job=job
        # self.email=f"{name}_350@gmail.com"

    @property
    def email(self):          # we make email function as attribute
        if self.name==None or self.job==None:
            return "Created Attributed successfully Deleted!!!"
        else:
            return f"{self.name}.{self.job}_350@gmail.com"

    @email.setter             # to set the function attribute
    def email(self,string):
        print("Setting now...")
        names = string.split("@")[0]       # returns 'Hello.World' of 0th position of list ["Hello.World","gmail.com"]
        self.name=names.split(".")[0]      # returns 'Hello' of 0th position of split list ["Hello","World"]
        self.job=names.split(".")[1]       # returns 'World' of 1st position of split list ["Hello","World"]
        pass

    @email.deleter
    def email(self):
        self.name=None
        self.job=None
    def show(self):
        return f"The name is {self.name} & email is {self.email}"

emp=Employee("Bhushan","Ambhore")
# print(emp.show())

# print(emp.email())     # if there is no decorator @property
# emp.name="wanda"
# print(emp.email())

# print(emp.name)        # just shown how attribute runs
print(emp.email)              # ran this function similar as running attribute

# We made email function as attribute. Now what if we want to set this attribute
# emp.email="Hello"      ------this throws error as we can't set like this unless we use @attribute_name.setter
emp.email="Hello.World@gmail.com"      # ------ we use @attribute.setter decorator as a result this get set
print(emp.email)
print("After Deletion")
# Now to delete that function attribute
# del emp.email      ------ this throws error as we cant delete like this unless there exist @attribute_name.delete
del emp.email        # as we use deleter it doesnt throwing error
print(emp.email)