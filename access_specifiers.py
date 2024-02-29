
class A():
    _val=32      # protected
    __pri=11     # private
    # def __init__(self,namee,sal,rol):
    #     self._name=namee       # protected
    #     self.__salary=sal      # private
    #     self._role=rol         # protected
    pass

class B(A):
    get=22
    pass

a=A()
b=B()

print(b._val)       # accessing protected
print(a._A__pri)    # accessing private variable by name mangling
print(b._A__pri)    # accessing private variable by name mangling
