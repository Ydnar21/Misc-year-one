"""
CSCI-141 Computer Science 1 Recitation Exercise
10-LinkedStruct
Filtering

Given a Python list of original fruits (as strings), and a Python
list of fruits to fliter out:

1. Convert the original and filter lists into linked structures.
2. Create a resulting linked structure that filters out the filtered
fruits from the original linked structure.
"""

from typing import Any, Union
from dataclasses import dataclass

@dataclass(frozen=True)
class Node:
    """
    A singly linked Node structure.
    :field value: the user defined value of any type
    :field next: the next Node this object points to (None if none)
    """
    value: Any
    next: Union[None, 'Node']

def to_string_rec_helper(node):
    """
    A helper function for making strings out of the values in the nodes in
    the linked structure.
    :param node: the current node in the linked struture
    :return:
    """
    if node is None:
        return ''
    else:
        return str(node.value) + ', ' + to_string_rec_helper(node.next)

def to_string_rec(node):
    """
    Convert a linked structure pointed to by node into a string that looks like
    a python list.
    :param node: the current node in the linked structure
    :return:
    """
    if node is None:
        return '[]'
    else:
        result = '[' + to_string_rec_helper(node)
        return result[:-2] + ']'

def contains_element(node, val):
    """
    Does the linked structure represented by the current node contain
    the value, val?
    :param node: current node in the linked structure
    :param val: the value to search for
    :return: whether the value is in the collection or not
    """
    if node is None:
        return False
    elif node.value == val:
        return True
    else:
        return contains_element(node.next, val)

def list_to_linked_struct(lst):
    """
    Convert a python list to a linked structure.
    :param lst: list to be converted
    :return: a linked structure equivalent to the passed in list
    """

def append_rec(val, node):
    if node==Node:
        return 0
    else:
        return Node(node.value, append_rec(val,node.next))
    new_lst= append_rec(3,lst)
    print(new_lst)

    return new_lst

def filter_linked_struct(original, filter):
    """
    Given an original linked structure and a linked structure
    of elements to filter, build and return a new structure
    with all the elements in filter removed.
    :param original: the linked structure being filtered
    :param filter: the linked structure of all the things to be
        removed from the original structure
    :return: a linked structure containing everything the original
        had that wasn't in the filter
    """
    # TODO: Activity 2
    return None

def main():
    """
    Test code for filtering.
    """

    # create the original list, and the list of words to filter out
    orig_list = ['apple', 'blueberry', 'cranberry' ,'pineapple', 'banana',
                 'orange', 'tangerine', 'papaya']
    filter_list = ['blueberry', 'pineapple', 'papaya']

    # Activity 1:
    # convert the original and filter lists into linked structures
    orig_linked = list_to_linked_struct(orig_list)
    filter_linked = list_to_linked_struct(filter_list)
    print('orig_linked:', to_string_rec(orig_linked))
    print('filter_linked:', to_string_rec(filter_linked))

    # Activity 2:
    # create the filtered linked structure
    result_linked = filter_linked_struct(orig_linked, filter_linked)
    print('result_linked:', to_string_rec(result_linked))

if __name__ == '__main__':
    main()