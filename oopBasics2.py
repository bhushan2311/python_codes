
class Employee():
    word_per_minute=90           # this is class variable share by its instances
    pass

kaushik=Employee()
hritik=Employee()

kaushik.name="Kaushik"
kaushik.salary=100

hritik.name="Hritik"
hritik.salary=150

print(kaushik.salary,kaushik.name,kaushik.word_per_minute)
print(hritik.salary,hritik.name,hritik.word_per_minute)

print(Employee.__dict__)                 # here the wpm is 90 in key value pair

Employee.word_per_minute=100             # here changed the wpm to 100 and it is common for all Employee objects
print("After changing class variable word_per_minute")
print("Hritik's word per minute",hritik.word_per_minute)
# hritik.word_per_minute=115               # wpm is changed only for hritik
# print(hritik.word_per_minute)

print(hritik.__dict__)             # this will print key value pair of hritik as dictionary
print(Employee.__dict__)           # here the wpm is 100 in key value pair