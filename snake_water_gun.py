import random

Comp=0
Human=0
Tied=0
print("\n....THIS GAME HAS 5 ROUNDS....")
def gun(h):
    l=["s","w","g"]
    ch=random.choice(l)
    if(ch==h):
        print("Round tied")
        global Tied
        Tied += 1
    elif(ch=='s' and h=='g' or ch=='w' and h=='s' or ch=='g' and h=='w' ):
        if(ch=='s'):
            print("You WON, Computer LOSE.\nComputer chooses SNAKE")
        elif(ch=='g'):
            print("You WON, Computer LOSE.\nComputer chooses GUN")
        else:
            print("You WON Computer LOSE.\nComputer chooses WATER")
        global Human
        Human += 1
    elif(ch=='w' and h=='g' or ch=='g' and h=='s' or ch=='s' and h=='w'):
        if(ch=='g'):
            print("You LOSE Computer WON.\nComputer chooses GUN")
        elif(ch=='s'):
            print("You LOSE Computer WON.\nComputer chooses SNAKE")
        else:
            print("You LOSE Computer WON.\nComputer chooses WATER")
        global Comp
        Comp += 1


for human in range(1,6):
    human = input("\n1.press 's' for Snake\n2.press 'w' for Water\n3.press 'g' for Gun\nChoose your option from above: ")
    c = gun(human)

if(Comp==Human):
    print("\nThis Match is tied\nNumber of tied rounds are:",Tied)
elif(Comp>Human):
    print("\nCOMPUTER WON this 5 rounds match."
          "As COMPUTER won maximum",Comp,"rounds\nYOU won",Human,"rounds\nNumber of tied rounds are:",Tied)
else:
    print("\nCongralutions!!!\nYOU WON this 5 rounds match. "
          "As YOU won maximum",Human,"rounds\nCOMPUTER won",Comp,"rounds\nNumber of tied rounds are:",Tied)



"""
d={"s":"Snake","w":"Water","g":"Game"}
for key,val in d.items():
    a=input("Enter w or s or g")
    c= gun(d.get(a))
"""

"""d={"s":"Snake","w":"Water","g":"Game"}
    ch=random.choice(d.get())"""