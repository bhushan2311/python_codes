"""
     Coroutines are mostly used in cases of time-consuming programs, such as tasks related to machine learning or
deep learning algorithms or in cases where the program has to read a file containing a large number of data.
In such situations, we do not want the program to read the file or data, again and again, so we use coroutines
to make the program more efficient and faster. Coroutines run endlessly in a program because they use a while
loop with a true or 1 condition so it may run until infinite time. Even after yielding the value to the caller,
it still awaits further instruction or calls. We have to stop the execution of coroutine by calling coroutine.close() function.
It is very crucial to close a coroutine because its continuous running can take up memory space as we have discussed in
Tutorial #75, related to function caching.

Coroutine Execution:-
Execution is the same as of a generator.When you call a coroutine, nothing happens. They only run in response to the next() and send() methods.
Coroutine requires the use of the next statement first so it may start its execution. Without a next() it will not start executing.
We can search a coroutine by sending it the keywords as input using object name along with send(). The keywords to be searched are send
inside the parenthesis.
"""
# import time
# def searcher():
#     string="hey i am very good and how are you."
#     print("--this statement Will print only once--")
#     time.sleep(2)
#
#     while(1):
#         letter=(yield)      # coroutine.      It receive the data sent by object_name.send(<data>)
#         if letter in string:
#             print("Yes..Its there!!")
#         else:
#             print("Its not there")
#
# search=searcher()
# print("Executing..Wait for couple of seconds")
# next(search)
# search.send("i am")                # send() used to send data to coroutine
# search.send("i am very")
# search.send("i an")
# search.close()                     # close() used to close the coroutine. After this send() will not runs it throws error StopIteration
# # search.send("i am very")      # throws error

# ----Quick Quiz---

def quiz():
    print("--Here are some invisible names--")
    names="Bhushan, Anjali, Sahil, Shivil, Shruti, Abhishek, Jayesh, Kaushik, Nobita, Harry, " \
          "Shinchan, Huvishk, Hritik, Nihal, Saurabh, Gautam, Yogesh, Rutuja , Devyani, Pandurang"

    while(True):
        name=(yield)
        if name in names:
            print("Available")
        else:
            print("not available")
    pass

q=quiz()
next(q)
q.send("Nihal")
q.send("Bhushan")
q.send("Aditya")
q.close()
# next(q)       # not running
# q.send("Nihal")