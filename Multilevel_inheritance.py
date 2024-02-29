
class ElectronicDevice():
    size=3
    def call(self):
        print("Late calling")
    pass

class PocketDevice(ElectronicDevice):          # inherits properties of ElectronicDevice class
    # size=2
    def call1(self):
        print("Fast calling")
    pass

class Phone(PocketDevice):                 # inherits properties of ElectronicDevice class as well as PocketDevice class
    size=1
    def call2(self):
        print("Calling with video chat")
    pass

ed=ElectronicDevice()
pd=PocketDevice()
p=Phone()

# p.call2()
p.call1()
p.call()

# pd.call1()
# pd.call()

print(p.size, pd.size)