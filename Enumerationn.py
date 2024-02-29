
# For printing Odd strings
l=["A","B","C","D","E","F"]
"""i=1                            # There is need to assign index 
for item in l:
    if i%2 != 0:
        print(item)        # output:- A C E
    i +=1"""                      # There is need to increment index

# printing above code using enumeration
for index,str in enumerate(l):            # there is neither need to assign index nor need to increment index
    if index%2 == 0:
        print(str)          # output:- A C E
