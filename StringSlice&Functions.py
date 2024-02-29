str = "abhayisgoodboy"
# # print(type(str))
# # print(str[0:3]) # print from index 0 i.e A to index 3 minus 1 i.e. h
# # print(str[:3])     # it by default assumes from 0 to 3 minus 1
#
# print(len(str))     # print length of the string i.e 17
# print(str[:178])         # if last limit index is not given or given but greater than String lenght, it will print whole String
# print("The gap is after every 1 string starting from 0 index:-",str[0::2])   # the 2 here after 2nd semicolon means it skips the 2 minus 1 i.e after every 1 index string
# print(str[:1])
# print(str[:-1])    # print upto o of boy
# print(str[-9:])    # it starts printing from left to right (count from extreme right i.e from 0)
# print(str[-9:-1])
#
# print(str.find("g"))           # shows the index of g
# print(str.isalnum())           # prints boolean true if there no space & false if there is no spaces in String
#
# str2= " u"
# print(str.join(str2))
#
# print(str.replace("good","best"))    # replaces good to best
#
# print(str.capitalize())           # Capitailse first letter
#
# print(str.upper())         # make all string captial
#
# print(str.isalpha())         # same as isalnum() function
#
# print(str.index("g"))      # same as function find()

n=int(input())
l=[]
for i in range(n):
    str=input()
    l.append(str)

# print(l)
for i in l:
    print(i[::2], i[1::2]) # Print odd and even characters

