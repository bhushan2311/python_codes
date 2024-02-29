# *args for list or tuple and **kwargs for dictionary. Here Astreik(*) means unpacking list,tuple and ** means unpacking dictionary

"""def name(a,b,c,d):
    print(a,b,c,d)

# if we want to add number of names out of these 4 positional arguments, then we must
# do changes here as well as in function definition arguments, so it is not proper approach...
name("War1","War2","War3","War4")"""

def name(string,*args,**kwargs):            # Arguments must be in order (positional_argument, * args, **kwargs)
    print(string)
    for item in args:
        print(item)
    print("\n------Avengers------")
    for k,v in kwargs.items():
        # print(k,"is a",v)
        print(f"{k} is a {v}")               # F-String


list=["Anil","Sahil","Rahul","Rani","Sujal"]              # Here we can add multiple names without making changes in function definition
j="This is normal argument & the names are..."
dict={"Steve":"Captain","Tony":"Ironman","Thor":"God of Thunder","Bruce":"Hulk"}

#Function Call
name(j,*list,**dict)                        # must give asterik