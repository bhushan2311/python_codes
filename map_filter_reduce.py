# -------------------------------MAP-----------------------------
# l1=["23","49","21","22","17"]
# print(int(l1[0])+2)         # converted particular string element into integer
#
# for i in range(len(l1)):
#     l1[i]=int(l1[i])                # converted each string element of list l1 into integer
#     # print(int(l1[i]))
#     # print(int(l1[i])+2)            # add 2 in each element which is converted from string into integer
# print(l1[0]+1)
#
# def add1(x):
#     return x+1
# m=list(map(lambda x:x*x,l1))              # each element of l1 mapped with x of lambda function and will return operation assigned
# print(m)

# l2=[23,12,23,54,12,45,47]
# m1=list(map(add1,l2))                    # each element of l2 mapped with x of add1 function and will return operation assigned
# print(m1)

# lis2=[1,2,3,4,5]
# def square(x):
#     return x*x
#
# def cube(x):
#     return x*x*x
#
# op=[square,cube]
#
# for i in lis2:
#     s1=list(map(lambda y:y(i),op))
#     print(s1)

# below tried logics don't work ie. shows errors
# def total(y):
#     return op(y)
# s1=list(map(total,lis2))
# s1=list(map(lambda y:y(lis2),op))
# print(s1)


# -------------------------------FILTER-----------------------------
lis1=[12,23,45,11,78,20,32,74]
# for item in lis1:                # normal
#     if(item%2==0):
#         print(item)

# def even(x):
#     return x%2==0
# s=list(filter(even,lis1))        # filters the list according to function whatever operation it returns
# print(s)
# -------------OR------------
# s=list(filter(lambda x:x%2==0,lis1))     # filters the list according to lambda function whatever operation it returns
# print(s)

# s=list(filter(lambda x:x>30,lis1))
# # s.sort()
# print(s)

# -----------------------------REDUCE----------------------------------
from functools import reduce

l1=[1,2,3,4,5]
#sum=0                  # normal
# for i in l1:
#     sum+=i
# print(sum)

t=reduce(lambda x,y:x+y,l1)                 # syntax:- reduce(function,sequence)
print(t)
