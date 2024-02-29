"""l1=[11,22,33,44,55,66,77,88,99]
for i in l1:                  # printing items of list using for loop
    print(i)"""

"""l2=[["abhishek",21],["aditya",22],["bhushan",23],["jayesh",24]]
for i,r in l2:             # printing item of items of list using for loop
    print(i,r)
d2=dict(l2)           # typecasted in dictionary by dict class
#print(type(d2))
#for i,r in d2:             # printing item of items of dictionary using for loop and this throws errors
  #  print(i, r)

for i,r in d2.items():
    print(i, r)"""

"""t=int(input("Enter number to get its table: "))
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(t," * ",i," = ",t*i)"""

# Quiz
# to print integers greater than 6
items = ["jhefk", 12, 45, 2,3,4,5,21,45,67, 8, 1, 3,int,float]
for i in items:
    if str(i).isnumeric() and i>6:
        print(i)
