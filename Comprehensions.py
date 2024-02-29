# Normally we use
# l=[]
# for i in range(1,101):
#     if i%5==0:
#         l.append(i)
# print(l)

# ------List Comprehensions------
# # l=[i for i in range(1,101)]
# # print(l)  # print 1 to 100
# l=[i for i in range(1,101) if i%5==0]
# print(l)

# dict= {}
# for k in range(5):
#     dict.update({k:f"item {k}"})
# print(dict)
# ------Dictionary Comprehension------
# dict={k:f"Item{k}" for k in range(5)}
# print(dict)
# dict1={v:k for k,v in dict.items()}
# print(dict1)


# ------Set Comprehension------
# set={k for k in [1,2,2,3,4,5,5,6]}    # set type
# # set=[k for k in [1,2,2,3,4,5,5,6]]        # list type
# print(type(set))
# print(set)


#
# def gen1(w):
#    for i in range(w):
#     if i%2==0:
#         yield i
# g=gen1(10)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # ------Generator Comprehension------
# gen=(i for i in range(10) if i%2==0)
# print(type(gen))    # type generator
# print(gen.__next__())
# print(gen.__next__())


# l=[]
# n=int(input("how many values:"))
# n1=print(f"Enter {n} values:")
# for i in range(n):
#     el=int(input())
#     l.append(el)
# print(l)

#---------Quick quiz-----------
# Ask User to what type of comprehension they want, give number of values and Enter values

print("What Comprehension you want?\n1.List comprehension \n2.Dictionary Comprehension \n3.Set Comprehension")
inp=int(input("Enter choice from above:"))
if inp==1:
    l=int(input("How many values you want in list?"))
    # l1=list(map(int,input().split()))
    print(f"Enter {l} values")
    list=[int(input()) for i in range(l)]
    print(type(list))
    print(list)

elif inp==2:
    l = int(input("How many key,values you want in dictionary?"))
    print(f"Enter {l} key,values")
    d={int(input("Val:")):int(input("Key:")) for i in range(l)}
    print(type(d))
    print(d)

elif inp==3:
    l = int(input("How many values you want in set?"))
    print(f"Enter {l} values")
    # list=[int(input()) for i in range(l)]
    # s={i for i in list}
    # OR
    s = {i for i in [int(input()) for i in range(l)]}
    print(type(s))
    print(s)
else :
    print("Enter Valid Choice!")








