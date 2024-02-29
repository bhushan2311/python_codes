"""import random
# for Random
r_n1=random.randint(1,10)      # simply print random no. from 1 to 10
print(r_n1)

# r_n2=random.random()         # this will generate random no from 0 to 1 including decimal point no.s
r_n2=random.random() * 2       # this will generate random no from 0 to 2 including decimal point no.s
r_n2=random.random() * 100     # this will generate random no from 0 to 100 including decimal point no.s
print(r_n2)


l=[[12,3],[3,1],[43,1],[33,1],["avi",2]]
r_n3=random.choice(l)            # print random choice from list l
print(r_n3)

#dict={"a":1,"b":2,"c":3,"d":4}
#r_n4=random.choice(dict)         # :((((

random.shuffle(l)           # shuffles the given parameter
print(l)

print(random.uniform(1,4))        # print random no between 1 to 4 including floating no. -- similar as random.random()"""


import platform          # gives info about operating system
x=platform.system()
print(x)
a=platform.node()
print(a)
q=platform.uname()
print(q)
# print(platform.processor())
