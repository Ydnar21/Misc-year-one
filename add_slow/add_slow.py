import threading
import time


global x


def add():
    global x
    for i in range(10000000):
        x += 1


def subtract():
    global x
    for i in range(10000000):
        x -= 1



if __name__ == "__main__":
    global x
    x = 0
    thread1 = threading.Thread(target=subtract())
    thread1.start()
    thread2 = threading.Thread(target=add())
    thread2.start()



    start = time.perf_counter()
    add()
    print(x)
    subtract()

    end = time.perf_counter()
    print(f'final x = {x}')
    print(f'elapsed time = {end - start}')

# 1. Measure the elaplsed time.
# 2. Run the add and subtract functions cuncurrently using threading.
# 3. Describe two issues and how would you fix it?
# I would fix the global variable in there because it doesnt seem to work the way it is. To fix it i would just make sure it is set to zero
# and maybe pass it into the methods.
# Well since the add and subtract function do the same thing except the opposite so naturally the only answer should be 0.
#I would fix this by either calling the add or subtract based on what the function.
# 4. Do you see any benefit in multithreading? WHy?
#yes it makes things go quicker and more efficiently. It is a little quick processing the program.