"""
file: linked_insort.py
author: Randy Dickersbach
description: homework
"""
import linked_code

def insert( value, lnk ):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """

    if lnk == None:
        return linked_code.LinkNode(value, None)
    if value < lnk.value:
        return linked_code.LinkNode(value,linked_code.LinkNode(value, lnk.rest))

    else:
        return linked_code.LinkNode(lnk.value, insert(value, lnk.rest))

def insort( lnk ):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """

    sort_list= None
    while lnk is not None:
        sort_list = insert(lnk.value, sort_list)
        lnk = lnk.rest

    return sort_list





def pretty_print( lnk ):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """

    lit=[]
    for i in range(linked_code.length_rec(lnk)):
        lit.append(linked_code.value_at(lnk, i))

    return str(lit)