# l=list(input().split())
# l.sort()
# print(l)
# print(" ".join(l))

# ------------------------------------------

# def sort_list(l):
#     return l[0]
#
# l=[["bhushan",89],["harry",78],["jay",67],["Aditya",22]]
# l.sort(key=sort_list)
# for i in l:
#     print(i[0])
#  OR
# Using Lambda
l=[["bhushan",89],["harry",78],["jay",67],["Aditya",22]]
l.sort(key=lambda l:l[0])
for i in l:
    print(i[0])