
# a=23
# b=43

# c=sum((a,b))         #this is also applicable
# print(c)

def add(a,b):               # def is used to define function
    """This addition function adds only two numbers"""    #here docString
    c=a+b
    return c

print(add.__doc__)               # calling docString
p=int(input("Enter one no."))
q=int(input("Enter second no."))
v=add(p,q)
print(v)