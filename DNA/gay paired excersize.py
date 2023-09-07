"""
CSCI-141 Computer Science 1 Recitation Exercise
11 - Stacks and Queues
Queue Exercise - College Things

Given a dictionary of things that are associated with different
colleges, create a queue and display the elements from the
dictionary that match the college, in the order they appear
in the dictionary.

For example:

$ python3 college.py RIT
college: RIT
queue size: 4
queue front: Rochester
queue back: Munson
queue elements:
Rochester
Ritchie
Hockey
Munson

This is the student starter code.
"""

from rit_queue import *

import sys      # sys.argv

# some things associated with different colleges
COLLEGE_THINGS = {
    # places
    'Rochester': 'RIT',
    'Pittsburgh': 'CMU',
    'Berkeley': 'UCB',
    'Cambridge': 'MIT',
    'Stanford': 'Stanford',

    # mascots
    'Scotty': 'CMU',
    'Tim': 'MIT',
    'Ritchie': 'RIT',
    'Oski': 'UCB',
    'Tree': 'Stanford',

    # sports
    'Football': 'Stanford',
    'Cross Country': 'MIT',
    'Baseball': 'CMU',
    'Basketball': 'UCB',
    'Hockey': 'RIT',

    # presidents
    'Jahanian': 'CMU',
    'Munson': 'RIT',
    'Reif': 'MIT',
    'Tessier-Lavigne': 'Stanford',
    'Napolitano': 'UCB',
}

def make_college_queue(college_things, college):
    """
    Given a dictionary of college things (key=string, value=string),
    create, make and return a queue that contains only the key things
    that match the college values in the dictionary.  For example:

    queue = make_college_queue(COLLEGE_THINGS, "Stanford"))

    Printing the queue would give:

    Queue(size=4,
          front=Node(value='Rochester', next=
                Node(value='Ritchie', next=
                Node(value='Hockey', next=
                Node(value='Munson', next=
                None)))),
          back=Node(value='Munson', next=
                None))

    :param college_things: dictionary of things (string) to college (string)
    :param college: the college (string)
    :return: queue of strings
    """
    # create an empty queue

    # TODO: Step 2

    # loop over the keys in the college_things dictionary.  for
    # any value that matches the college, enqueue the key onto
    # the queue

    # TODO: Step 3

    # return the queue

    # TODO: Step 4

def main():
    """
    The main program reads in the college string, creates the
    queue of college things for that particular college, and
    then displays the things.
    """
    if len(sys.argv) != 2:
        print('Usage: python3 college.py COLLEGE')
    else:
        # get the college name from the command line
        college = sys.argv[1]
        print('college:', college)

        # get the queue of things for the particular college by
        # calling make_college_queue with the dictionary of college
        # things, COLLEGE_THINGS, and the college string, college

        # TODO: Step 1

        # print out the queue size, front and back elements

        # TODO: Step 5
        print('queue size:', None)
        print('queue front:', None)
        print('queue back:', None)

        # while the queue is not empty, print the element at the
        # front of the queue and then dequeue it
        print('queue elements:')

        # TODO: Step 6

if __name__ == '__main__':
    main()