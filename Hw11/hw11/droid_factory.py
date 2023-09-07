from cs_queue import  *
from dataclasses import dataclass
from typing import Any, Union
from node import *

@dataclass
class Droid:
    head:   bool
    body:   bool
    arms:   bool
    legs:   bool
    digit:  int

#Task 2-
def unloading (file_name):
    """
    This opens the file and goes through each line then making the queue.
    :param file_name: the file that wants to be tested
    :return: returns the Queue
    """
    queue = make_empty_queue()
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            enqueue(queue,line)
    return queue

def creating_droid(file_name):
    """
    Create the droids and each part is a boolean to check if it has the part or not
    :param file_name: the file that wants to be tested
    :return: nothing it just prints out the commands shown in the homework
    """
    print(unloading(file_name))
    droid_part = unloading(file_name)
    droid_serial = 420
    print(droid_serial)
    droid = Droid(False, False, False,False,droid_serial)
    check = False
    while check is not True:
        if droid_part.size != 0:
            if front(droid_part) == "head":
                if droid.head != True:
                    print("Attaching a head...")
                    droid.head = True
                    dequeue(droid_part)
                else:
                    temp = dequeue(droid_part)
                    enqueue(droid_part, temp)
                    print("Placing unneeded part back on belt ",temp)


            elif front(droid_part) == "arms":
                if droid.arms != True:
                    print("Attaching arms...")
                    droid.arms = True
                    dequeue(droid_part)
                else:
                    temp = dequeue(droid_part)
                    enqueue(droid_part,temp)
                    print("Placing unneeded part back on belt ",temp)

            elif front(droid_part) == "legs":
                if droid.legs != True:
                    print("Attaching legs...")
                    droid.legs = True
                    dequeue(droid_part)
                else:
                    temp = dequeue(droid_part)
                    enqueue(droid_part, temp)
                    print("Placing unneeded part back on belt ",temp)


            elif front(droid_part) == "body":
                if droid.body != True:
                    print("Attaching body...")
                    droid.body = True
                    dequeue(droid_part)
                else:
                    temp = dequeue(droid_part)
                    enqueue(droid_part, temp)
                    print("Placing unneeded part back on belt ",temp)


            if droid.head == True and droid.arms == True and droid.body == True and droid.legs == True:
                print("Droid ", droid_serial, " has been assembled")
                if droid_part.size != 0:
                    check= False
                    droid.body, droid.head, droid.legs, droid.arms = False, False, False, False,
                    droid_serial += 1
                else:
                    check = True


            else:
                check = False
        else:

            print("All Droids have been assembled for the amount of parts given")
            check = True


def test1():
    """
       test function 1
       :return: prints the droid information
       """
    file_name= "7_parts.txt"
    unloading(file_name)
    creating_droid(file_name)
def test2():
    """
    test function 2
    :return: prints the droid information
    """
    file_name= "droid_parts_5.txt"
    unloading(file_name)
    creating_droid(file_name)

def main():
    file_name = input("What is the file name: ")
    unloading(file_name)
    creating_droid(file_name)

#main()
test1()
test2()
print("All Droids have been assembled. Time to go to PARTAYY")