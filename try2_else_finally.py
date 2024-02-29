
def el(a,b):
    try:
        print(f"{a}/{b} is {a/b}")
    except Exception as e:
        print("Error Occured:-",e)
    else:
        print("Yippie..No Division by Zero")  # this get print only when there is no error occurs

    finally:         # Either error occurs or not finally block will get print and it is also known as 'code cleaner'
        print("The End")

el(22,0)