class e():
    def __init__(self, q):
        self.q = q
E = e(7)


class Student():
    std = 7

    # (CONSTRUCTOR)this will get executed as soon as object/s is made
    def __init__(self, namee, idd, divv):  # here __init__ will receive obj as argument to self
        self.name = namee
        self.id = idd
        self.div = divv
        # print(namee)             # will run for both ram and sham
        # print(f"Name is {self.name}, id is {self.id}, div is {self.div}")      # will run for both objects ie. for ram and sham
        # print("This is constructor")    # this will print as soon as object/s is made

    def meth(self):
        print(
            f"Name is {self.name}, id is {self.roll}, div is {self.section}")  # will run for ram if call by ram similarly for sham


ram = Student("Ram", 23, "A")  # obj(ram) will pass as argument to constructor's and method's self
sham = Student("Sham", 21, "B")  # obj(sham) will pass as argument to constructor's and method's self

# print(ram.name,ram.id,ram.div)      # from constructor
# print(sham.div)

ram.name = "RAM"
ram.roll = "78"
ram.section = "A1"

sham.name = "SHAM"
sham.roll = 213
sham.section = "B1"

# ram.meth()
# sham.meth()

# this will run for 'RAM' name not for constructor 'ram' name only if there is ram.name="RAM" otherwise it will run for constructor name
print(ram.name)
