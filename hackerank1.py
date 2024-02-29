# l=[[1,2],[3,4]]
# for i in l:
#     print(i[1])

# l=[]
# n=int(input())
# for i in range(n):
#     l1 = []
#     name=input()
#     mark=float(input())
#     l1.append(name)
#     l1.append(mark)
#     l.append(l1)
# # print(l)
# l.sort(key=lambda l:l[1])
#
# print(l)    # -----------
# l2=[]          # for storing all score except last score/es
#
# for i in l:
#     if i[1]==l[0][1]:
#         continue
#     else:
#         l2.append(i)
# print(l2)    # -----------
# l3=[]        # for storing all last second place scores
# for i in l2:
#     if i[1]==l2[0][1]:
#         l3.append(i)
#
# l3.sort(key=lambda l3:l3[0])
# print(l3)    # -----------
# for i in l3:
#     print(i[0])
# --------------------------------------------------

# n1=int(input())
# t=tuple(map(int,input().split()))
# print(t.__hash__())
# # OR
# n=int(input())
# t=hash(tuple(int(i) for i in range(n)))
# print(t)

# ----------------------------------------------------

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
    def __init__(self,firstName,lastName,idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores=scores
        pass

#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):
        avg=sum(scores)//len(scores)
        print(avg)
        if avg>=90 and avg<=100:
            return 'oo'
        elif avg>=80 and avg<90:
            return 'E'
        elif avg>=70 and avg<80:
            return 'A'
        elif avg>=55 and avg<70:
            return 'P'
        elif avg>=40 and avg<55:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())










