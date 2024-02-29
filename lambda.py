# lambda functions or Anonymous Function or one liner function

# def minus(a,b):
#     return a-b
#
# print(minus(9,3))

# syntax :- function name = lambda arg1,arg2 : operation

# example 1
# minus = lambda a,b : a-b
# print(minus(9,3))

# l=[23,1,45,22,98]
# l.sort()
# print(l)

#------------------------------------------------

def list_sort(l):
    return l[1]

l=[[23,12],[2,1],[11,65],[7,3]]
l.sort(key=list_sort)
print(l)         # this sorts element according to 1th index of list of list

# using lambda function
# l=[[23,12],[2,1],[11,65],[7,3]]
#
# l.sort(key=lambda l:l[1])
# print(l)