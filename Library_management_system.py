
# class Library:
#
#     def __init__(self,name,args):
#         self.name=name
#         self.list=args
#         pass
#
#     def display_book(self):
#         print(f"--- Available Books in {self.name} Library are ---")
#         for i in self.list:
#             print(i)
#
#     def lend_book(self):
#         ch=input("Enter book name you want to lend:")
#         if ch in self.list:
#             self.list.remove(ch)
#         else:
#             print("Sorry the Book already is issued by somebody!!!")
#         pass
#
#     def add_book(self):
#         add1=input("Enter the book name you want to add:")
#         self.list.append(add1)
#         print(f"The book {add1} has been Successfully added in the Library")
#         pass
#
#     def return_book(self):
#         return1 = input("Enter the book name you want to return:")
#         self.list.append(return1)
#         print(f"The book {return1} has been Successfully returned in the Library")
#         pass
#
# if __name__ == '__main__':
#     print("----------Welcome to the Library----------")
#     original_list = ['Maths', 'Science', 'English', 'Marathi', 'Geography']
#     lib = Library("Shiv", original_list)
#     lib.display_book()
#     while(True):
#         print("\n1.Lend Book\n2.Add book\n3.Return Book\n4.Display Book")
#         ch=int(input("Enter your Choice:"))
#         if ch==1:
#             lib.lend_book()
#         elif ch==2:
#             lib.add_book()
#         elif ch==3:
#             lib.return_book()
#         elif ch==4:
#             lib.display_book()
#         else:
#             print("Please Enter Valid Choice")
#
#         ch=input("Enter Any key to continue or only q to Quit:")
#         if ch == "":
#             continue
#         elif ch == "q":
#             exit()



class Library:

    def __init__(self,name,args):
        self.name=name
        self.list=args
        self.lendict={}
        pass

    def display_book(self):
        print(f"--- Available Books in {self.name} Library are ---")
        for i in self.list:
            print(i)

    def lend_book(self,book,user):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("Thank u. You can take the book.")
        else:
            print(f"Sorry! The book taken by already {self.lendict[book]}.")

    def add_book(self):
        add1=input("Enter the book name you want to add:")
        self.list.append(add1)
        print(f"The book {add1} has been Successfully added in the Library")
        pass

    def return_book(self):
        try:
            return1 = input("Enter the book name you want to return:")
            self.lendict.pop(return1)
            print(f"The book {return1} has been Successfully returned in the Library")
        except Exception as e:
            print("Maybe the Book which you are trying to return is already in Library OR"
                  " Maybe you are trying to add new book then try choice 3.Add Book")
        pass

if __name__ == '__main__':
    print("----------Welcome to the Library----------")
    original_list = ['Maths', 'Science', 'English', 'Marathi', 'Geography']
    lib = Library("Shiv", original_list)
    lib.display_book()
    while(True):
        print("\n1.Lend Book\n2.Add book\n3.Return Book\n4.Display Book")
        ch=int(input("Enter your Choice:"))
        if ch==1:
            book=input("Enter book name you want to lend:")
            name=input("Enter name")
            lib.lend_book(book,name)
        elif ch==2:
            lib.add_book()
        elif ch==3:
            lib.return_book()
        elif ch==4:
            lib.display_book()
        else:
            print("Please Enter Valid Choice")

        ch=input("Enter Any key to continue or only q to Quit:")
        if ch == "":
            continue
        elif ch == "q":
            exit()


