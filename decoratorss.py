# def f1(x):
#     return x+2
#
# def f2(x1):
#     print(f"Value must be greater than 5 and the value is {x1}")
#     return f1(x1)
# f3=f2
# del f2           # just deleted to know whether f3 will run or not
# print(f3(7))
# #  OR
# f3=f2(7)
# del f2
# print(f3)

# ---------------harry's example from below-----------------

# def fun1():
#     print("sunrising")
# fun2 = fun1                  # assigned one function_name into new function_name
# del fun1            # just deleted to know whether fun2 will run or not
# fun2()                # function_name() ----> function calling

# def function(fun):
#     fun("Hello")
#
# func=function
# func(print)

# ----------------------- DECORATORS --------------------------
n=int(input("enter no."))

def func1(funct):
    def exec(n):
        print("Open now ")
        funct(n)
        print("Opening")
    # return exec()         # returning call
    return exec             # returning function name

@func1                     # @function_name ---> Decorator
def open(n):
    print("OKK",n)
open(n)
# open=func1(open)    # dont call open() if function is returning function call
# open()            # only if function is returning function name
# OR
# func1(open)                     # will run only if there is function 'call' ie. exec() parenthesis is imp or ie. returning function call
# print(func1(open))                # there must not be parenthesis ie. no function call instead it must return function name

# @func1
# def NO():
#     print("Nooo!!")







