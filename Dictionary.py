"""# Dictionary is nothing but Key-Value Pair

d1={"Shubham":201,"Rahul":205,"Sai":210,"Lovish":217,"Krutika":212,"Rasika":219,}
#print(d1)
# print(d1["Lovish"])          # will print its mapping value
# d1["Divya"]=222        # updation
# d1[221]="Vrushal"      # updation
# print(d1)
#d1.pop("Sai")
#d1.popitem()
#d2=d1
#print(d2.get("Krutika"))
#d2=d1.copy()
#print(d2.values())
#print(d1.items())

# inp=input("Enter name to get Roll no. ")   # Taking input(Key) from user and printing its value
# print(d1.get(inp))

# d1.update({"Mrunali":227})      # updation
# print(d1.items())
#
# del d1["Shubham"]
# print(d1)
d={"s":"Snake","w":"Water","g":"Game"}
for key,val in d.items():
    a=input("Enter w or s or g")
    print(d.get(a))
     # c= gun(d.get(a))"""

dict={}

# dict.update({0:'s'})
# print(dict)
#
# if 1 not in dict.keys():
#     print("no")
#     name=input("Enter name")
#     dict.update({1:name})
# else:
#     print("yes")

d1={"Shubham":201,"Rahul":205,"Sai":210,"Lovish":217,"Krutika":212,"Rasika":219,}

del d1["Shubham"]
print(d1)

print(divmod(2,1),2/1)

l=[2,3,4]
print(list(reversed(l)))
d={33:"e",22:"uu"}

print('xyyzxyzxzxyy'.count('yy',1))

d.popitem()
print(d)