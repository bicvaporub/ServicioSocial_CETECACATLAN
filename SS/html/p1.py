import threading

def print_square(num):
    print("Square: {}".format(num *num))

def print_cube(num):
    print("Cube: "+str(num * num * num))

t1 = threading.Thread(target=print_cube, args=(10,))
t2 = threading.Thread(target=print_square, args=(10,))   

print("Hello World")

t1.start()
t2.start()

t1.join()
t2.join()

print("Bye World")