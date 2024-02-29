# ---- By list concept ----
# l=[]
# print("How many inputs do you want?")
# n=int(input("Enter:"))
# print(f"Enter {n} inputs: ")
# for i in range(n):
#     inp=int(input())
#     l.append(inp)
# print(l)

# ---- By mapping ----
# print("Enter no. values and give space between.")
# l1=list(map(int,input().split(",")))
# print(l1)

# ------ By list comprehension ------
a=int(input("How many values you want to enter?\n"))
print(f"Enter {a} values")
l=[int(input()) for i in range(a)]
print(l)

