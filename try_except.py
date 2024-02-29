
# this is executing properly without return
# def div():
#     try:
#         a=int(input("Enter 1 no."))
#         b=int(input("Enter other no."))
#         c=a+b
#         # try:
#         #     c=a/b
#         # except Exception as e:
#         #     print(e)
#         print(c)
#     except Exception as e:
#         print("Please Enter Integer as Input")
#     print("End of Code")
# div()



def div():
    a=int(input("Enter 1 no."))
    b = int(input("Enter other no."))
    c = a / b
    return c
    #try:                                # getting error in returning c to call
    #     a=int(input("Enter 1 no."))
    #     b=int(input("Enter other no."))
    #     c=a/b
    # except Exception as e:
    #     print("Please Enter Integer as Input")
    # return c

# print(div())
try:
    print(div())                        #
except Exception as e:
    print("Please Enter Integer as Input :(")
print("End of Code")