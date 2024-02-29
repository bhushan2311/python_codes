var1 = "String"
var2 = 5
var3 = 32.7
var4 = "5 "

# print(type(var1))       #this shows its type
print(var1, var2)
print(var2 + var3)

# to add string and int variable there is need of type cast
print(var4 + str(var2))  # this will add string + string as integer typecasted intostring
print(int(var4) + var2)  # this will add int+int as string typecasted into int

print(var1 + var4 + str(var3))  # this will add string plus string as float typecasted into string
print(float(var4) + var3)  # string typecasted into float, this will add float plus float

# Taking input from user
print("Enter one number")
# inpnum=input()             #this will assume as string input as there it is default until we provide it int or float
inpnum = int(input())
print("Enter Second number")
# inpnum1=input()            #this will assume as string input as there it is default until we provide it int or float
inpnum1 = int(input())
print(inpnum + inpnum1)
