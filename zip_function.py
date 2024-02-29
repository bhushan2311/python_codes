# a=[1,2,3,4]
# b=[5,6,7,8]
#
# z=zip(a,b)
# print(z)   # will print zip object
# z1=list(z)  # type casted into list
# # print(sum(z1[0]))     # will add elements of index 0
# print(z1)
#
# name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
# roll_no = [4, 1, 3, 2]
# marks = [40, 50, 60, 70]
#
# # using zip() to map values
# mapped = zip(name, roll_no, marks)
# mapped = set(mapped)
#
# print(mapped)

# a=[1,2,3,4]
# b=[5,6,7,8]
# #----- using for loop ------
# for k,v in zip(a,b):
#     print(k,v)
#
# #----- unzipping-----
# c=[[33,44,66],[21,34,54]]
# u=zip(*c)
# print(list(u))  # will print list of tuples
# # print(tuple(u)) # will print tuple of tuples

# ---- calculating in pairs ------
#       s1  s2   s3  s3  s4
sub1 = [89 ,90 , 78, 93, 80]
sub2 = [90 ,91 , 85, 88, 86]
sub3 = [91 ,92 , 83, 89, 90.5]

# sub1 = list(map(float,input().split()))
# sub2 = list(map(float,input().split()))
# sub3 = list(map(float,input().split()))

z=list(zip(sub1,sub2,sub3))
# print(z)          # output :-  [(89, 90, 91), (90, 91, 92), (78, 85, 83), (93, 88, 89), (80, 86, 90.5)]
for i in z:         # indexes(i) :-   0               1             2             3             4
    print(sum((i))/3)
# OR
# for a,b,c in zip(sub1,sub2,sub3):
#     # print(a,b,c)         # will print sub1,sub2,sub3 in vertical
#     print(sum((a,b,c))/3)

# ---------------------------------------

# stu,sub=input().split()
# student=int(stu)
# subject=int(sub)
# print(type(subject))
# l=[]
# for i in range(subject):
#     a=list(map(float,input().split()))
#     l.append(a)
#
# # for i in zip(*l):
# #     print(sum(i))
#
# u=list(zip(*l))
# for i in u:
#     print(i)
#     print(len(i))
#
#     # s=sum(i)/3
#     # print("{:.2f}".format(s))


