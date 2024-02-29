
# x=23
# def fun1():
#     x=66
#     print(x)        # print x of fun1() scope
#
# fun1()
# print(x)            # print x of outside fun1() scope

# x=54
# def fun2():
#     global x         # by assigning global in this function, this function has right to change x globally
#     x=2
#     print(x)
#
# fun2()
# print(x)

x=90
def fun3():
    x=23
    def fun4():
        global x             # this will update x=90 to x=55 globally
        x=55
        print(x)
    fun4()             # necessary to call nested function, otherwise fun4() will not run
    print(x)

fun3()
print(x)