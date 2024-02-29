# our custom created module

a=23

def add(b,c):
    return b+c

mul=lambda x,y: x*y

print(__name__)             # will show the name of this module in the file where this module(file) get imported.. And will print __main__ in this file

# by using this, the function and print stetement written below will not get executed
# in the file which importing this module util you call them there
if __name__ == '__main__':
    b=3
    print(f"Hello there {a}")
