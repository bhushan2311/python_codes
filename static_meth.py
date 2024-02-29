class Student():

    def subject(self,sub,namee):
        # self.name=namee
        return f"The name is {namee} & Subject chosen by {namee} is {sub}"

    @staticmethod
    def marks(mark,total):
        print("Marks is",mark,"out of",total)

ram=Student()

print(ram.subject("Biology","RAM"))
ram.marks(78,100)
