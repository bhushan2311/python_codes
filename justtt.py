# t=int(input())
# for i in range(t):
#     n=int(input())
#     string=str(n)
#     if int(string[0])>1:
#         print("1"+string)
#     elif int(string[0])==1:
#         print(string[0:1]+"0"+string[1:len(string)])
#------------------------------------------------------
# t=int(input())
# for i in range(t):
#     a=input()
#     if(a[0]>"1"):
#         print("1" + str(a))
#     elif(a[0]=="1"):
#         print(a[0]+"0"+a[1:len(a)])

# def greater(a,b,c):
#     if (a>b):
#         if(a>c):
#             print(a)
#     elif(b>a):
#         if(b>c):
#             print(b)
#     elif(c>a):
#         if(c>b):
#             print(c)
#
# t=int(input())
# for i in range(1,t+1):
#     n1 = int(input())
#     n2 = int(input())
#     n3 = int(input())
#     greater(n1, n2, n3)

# t=int(input())
# for tc in range(t):
#    x = list(map(int, input().split()))
#    x.sort()
#    print(x[1])

# t=int(input())
# for i in range(1,t+1):
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     l = [a, b, c]
#     l.sort()
#     print(l[1])


# n = int(input())
# if n%2!=0 or n%2==0 and n>=6 and n<=20:
#     print("Wierd")
# elif n%2==0:
#     if n>=2 and n<=5 or n>20:
#         print("Not Weird")

# inp=int(input())
# for i in range(inp):
#     print(i*i)
# inp=int(input())
# l=[print(i*i) for i in range(inp)]

#------------------ Leap Year ----------------------
# def is_leap(year):
#     # Write your logic here
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
#
#     return leap
# year = int(input())
# print(is_leap(year))

# n = int(input())
# for i in range(1,n+1):
#     print(i,end="")

# n = int(input())
# l=[]
# for i in range(n):
#     el=int(input())
#     l.append(el)
# l.sort()
# l.reverse()
# print(l)

# n = int(input())
# l = (input().split())
# l.sort()
# l.reverse()
# # print(l)
#
# def is_less():
#     for i in range(len(l)):
#         if l[i] < l[0]:
#             print(l[i])
#             break
# # print(is_less())
# is_less()

# n = int(input())
# l=list(map(int,input().split()))
# l.sort()
# l.reverse()
# for i in l:
#     if i<l[0]:
#         print(i)
#         break
#-------------------------------------------------------
# n=int(input())
# dict={}
# for i in range(10):
#     name=input()
#     marks=list(map(float,input().split()))
#     dict.update({name:marks})
#     if i<n-1:
#         continue
#     else:
#         naam=input()
#         s=dict[name]
#         print(sum(s)/3)
#         break
# OR
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for i in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     a=student_marks[query_name]
#     avg=sum(a)/3
#     average="{:.2f}".format(avg)
#     print(average)
#     # print(student_marks)
# d={} ############################################
# name,*mark=input().split()
# scores=list(map(int,mark))
# d[name]=scores
# print(d)#########################################
"""a,b,c=52,56,60
c=(a+b+c)/3
c1="{:.2f}".format(c)
print(c1)
float=2.12467
form="{:.2f}".format(float)
print(form)"""
# OR
# d={}
# class student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def update(self):
#          d.update({self.name:self.marks})
#
#     def avg(self):
#         # print(d)
#         name=input()
#         a=d[name]
#         print(sum(a)/3)
#         # avg=sum(self.marks)/2
#         # print(avg)
#
# if __name__ == '__main__':
#     no=int(input())
#     for i in range(10):
#         nam=input()
#         m = list(map(float, input().split()))
#         stu = student(nam,m)
#         stu.update()
#         if i < no-1:
#             continue
#         else:
#             stu.avg()
#             break
#-------------------------------------------------------------------------
# def solve(meal_cost, tip_percent, tax_percent):
#     # Write your code here
#     tip=(meal_cost * tip_percent)/100
#     tax=(tax_percent * meal_cost)/100
#     total_cost=meal_cost+tip+tax
#     # tip = (meal_cost * tip_percent) / 100
#     # tax = (meal_cost * tax_percent) / 100
#     # totalCost = int(round(meal_cost + tip + tax))
#     # print(totalCost)
#     print(int(round(total_cost)))
#
# if __name__ == '__main__':
#     meal_cost = float(input())
#
#     tip_percent = int(input())
#
#     tax_percent = int(input())
#
#     solve(meal_cost, tip_percent, tax_percent)


# class Person:
#     def __init__(self,initialAge):
#         # Add some more code to run some checks on initialAge
#         self.initialAge=initialAge
#
#     def amIOld(self):
#         # Do some computations in here and print out the correct statement to the console
#         if self.initialAge<0:
#             print("Age is not valid, setting age to 0.")
#             self.initialAge=0
#             print("You are young.")
#
#         elif self.initialAge>=0 and self.initialAge<13:
#             print("You are young.")
#
#         elif self.initialAge>=13 and self.initialAge<18:
#             print("You are teenager.")
#
#         else:
#             print("You are old.")
#
#     def yearPasses(self):
#         # Increment the age of the person in here
#         self.initialAge = self.initialAge + 1
#         pass
#
# t = int(input())
# for i in range(0, t):
#     age = int(input())
#     p = Person(age)
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()
#     p.amIOld()
#     print("")
    #OR
    # if age<0:
    #     print("Age is not valid, setting age to 0.")
    #     age=0
    #     print("You are young.")
    #     p.yearPasses()
    #
    # elif age>0 and age<13:
    #     print("You are young.")
    #     p.yearPasses()
    #     p.amIOld()
    #
    # elif age>=13 and age<18:
    #     print("You are teenager.")
    #     p.yearPasses()
    #     p.amIOld()
    #
    # else:
    #     print("You are old.")
    #     p.yearPasses()
    #     p.amIOld()

# e = int(input())
# l = []
# for i in range(3):
#     inp, *a = input().split()
#     a1 = list(map(int, a))
#     l.insert(a1[0], a1[1])
# print(l)
# inp,u=input().split()
# u1=int(u)
# l.remove(u1)
#
# i,v=input().split()
# v1=int(v)
# l.append(v1)
#
# w,u=input().split()
# w1=int(u)
# l.append(w1)
#
# cmd=input()
# if cmd=="sort":
#     l.sort()
#     print(l)
#
# cm=input()
# if cm=="pop":
#     l.pop()
#
# c=input()
# if c=="reverse":
#     l.reverse()
#     print(l)

# l.append(e)
# l.sort()
# l.pop()
# l.reverse

# def split_and_join(line):
#     l=line.split()
#     return "-".join(l)
#     # write your code here
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# -------------------Exception------------------------
# n=int(input())
# l=[]
#
# for i in range(n):
#     a, b = input().split()
#     l.append(a)
#     l.append(b)
# print(l)
# # print(int(l[0])/int(l[1]))
#
# for i in l:
#     try:
#         print(int(l[0]) // int(l[1]))
#     except Exception as e:
#         print("Error Code:",e)
#     l.remove(l[0])
#     l.remove(l[0])
# try:
#     print(int(l[0])//int(l[1]))
# except Exception as e:
#     print("Error Code:",e)
# # l=[23,324 ,2143,21]
# # l.remove(l[0])
# # l.remove(l[0])
# # print(l)
#  OR
# for i in range(int(input())):
#     try:
#         a, b = map(int,input().split())
#         print(a//b)
#     except Exception as e:
#         print(e)
# -------------------------------------------------------

# if __name__ == '__main__':
#     n = int(input())
#     l = []
#     v=list(map(int,input().split()))
#     v.reverse()
#     for i in v:
#         print(i,end=" ")

# ---------------------------------------------------------

# phbk={}
# for i in range(int(input())):
#     name,no=input().split()
#     numb=int(no)
#     phbk.update({name:no})
# while(True):
#     # try:
#     #     e = input()
#     #     if e in phbk:
#     #         print(f"{e}={phbk.get(e)}")
#     #     else:
#     #         print("Not Found")
#     # except:
#     #     break
#     # OR
#     try:
#         naam=input()
#     except EOFError as e:
#         break
#     if naam in phbk:
#         print(f"{naam}={phbk.get(naam)}")
#     else:
#         print("Not found")

# -------------------Bubble sort------------------------
