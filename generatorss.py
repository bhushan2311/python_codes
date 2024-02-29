"""
iterable - __iter__() or __getitem__()
-> iterables are the objects that can be placed inside a loop and are capable of returning one variable at a time.
   In simple term, we can say that iterables are objects capable of iteration. E.g. List,String,Tuple
    for i in range (a):  # here a is iterable and it is capable of iteration
       print(i)

iterator - __next__()
->  iterator can be defined as objects that does iterations on iterable. Meaning that it can be move from character to character(using __next()__ method)
    doing iteration.  # Generators are iterators

iteration -> the phenomenon that occurs by the combination of two concepts(ie. iterable and iterator) is known as iteration.
"""

def genErator(x):
    for i in range (x):    # x is iterable
        yield i

g=genErator(2)       # g is iterator
# print(g)
print(g.__next__())
print(g.__next__())

s="String"               # iterable
# for char in s:
#     print(char)
p=iter(s)            # p is iterator
print(p.__next__())
print(p.__next__())
print(p.__next__())


# c=233423
# for i in c:
#     print(i)      # throws error as int object is not iterable