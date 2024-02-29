"""i=0

while(i<100):
    print(i+1, end=" ")
    if(i==91):
        break
    i+=1"""

"""i=1
while(1):
    if(i<20):
        i += 1
        continue
    print(i)
    if (i==22):
        break
    i += 1"""

# Quiz
# Taking input from user until they enter number greater than 100

"""while(True):
    n = int(input("Enter number"))
    if(n>100):
            print("Congratulation, you entered number greater then 100")
        break"""

while(True):
    n = int(input("Enter number"))
    if(n<100):
        continue
    else:
        print("Congratulation, you entered number greater then 100")
        break