# --------------List is Mutable(can change)---------------------
grocery = ["oil", "maggie", "kissan_jam", "Shampoo", "Soap"]
#          0      1          2           3        4
# print(grocery)
# grocery.append("Powder")     # add at the end
# print(grocery)

# Slicing in List
# print(grocery[:])     # by default it takes [0:5]
# print(grocery[2:4])
# print(grocery[:-3])       # output will print from from 0["oil"] and (count{from 0,-1,..} from right to left ie. from["Soap"]) and stop where -3 index arrive..
# print(grocery[::2])
# print(grocery[1:3:-1])    # must be -1 in third parameter of sq.bracket if there exist other parameter in sq.barcket otherwisse it will print-->[]

# some functions on list
num = [23, 42, 67, 11, 2, 4]

# num.append(100)
# num.append(200)
# num.append(300)
# print(num)              # will add all above appended numbers at last of the list

# num.sort()    # sort here
# num.reverse()  # reverse here
print(num)     # first it will sort then it will reverse
print("-------")
num.remove(42)
print(num)
# num.clear()
# num.insert(3,99)      # insert 99 at index 3

# print(num.pop())
# print(num.pop(2))

# num[3]=55         #replaces element --> [23,42,67,55,2,4]
# print(num)

#del num[0]
#print(num)

# -------------Tuples are immutable(cannot change)------------

tpl=(11,22,33,44,55)
# tpl=(1,)
# print(tpl)

#del tpl[0]      # Error--->'tuple' object doesn't support item deletion
#print(tpl)

a = 1
b = 2
print("before swapping")
print(a, b)

# temp=a
# a=b
# b=temp
a, b = b, a  # simple way of swapping
print("after swapping")
print(a, b)
