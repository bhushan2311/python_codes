
l=[1,2,3,4,5,6]
for i in l:
    if i==0:
        break
    else:
        print(i)
else:         # control will not comes in else, if loop encounters break statement
    print("Executed")