from _thread import start_new_thread
from time import sleep

threadID = 1
waiting = 2

def factorial(n):
    global threadID
    rc = 0
    if n < 1:
        print("{}: {}".format('\nThread',threadID))
        threadID = threadID + 1
        rc = 1
    else:
        returnNumber = n * factorial(n - 1)
        print("{} != {} >".format(str(n),str(returnNumber)))
        rc = returnNumber
    return rc

start_new_thread(factorial,(5, ))
start_new_thread(factorial,(4, ))

print("Waiting gor threads to return...")
sleep(waiting)

import threading 
def multiply(num,count):
  if( count < 11):
     print(num," * ",count," = ",num * count)
     return multiply(num,count + 1)
  else:
    return 1
t1 = threading.Thread(target=multiply, args=(10,2))
t2 = threading.Thread(target=multiply, args=(10,3))

print("Hello world")

t1.start()
t2.start()

t1.join()
t2.join()

print("Bye world")