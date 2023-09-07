from dataclasses import dataclass
from typing import Any, Union
import linked_code
"""
Author:Randy Dickersbach
File:dna.py

"""

@dataclass(frozen=True)
class LinkNode:
    """
    An object type to hold any kind of data that can be put into a sequence
    """
    value: Any
    rest: Union["LinkNode", None]
def convert_to_string(dna):
    """

    :param dna: dna sequence
    :return: a string of the linked list
    """
    dna_string = ""
    if dna is None:
        return ''
    else:
        dna_string += (dna.value) + convert_to_string(dna.rest)
    return dna_string


def convert_to_nodes(dna1):
    """

    :param dna1: dna sequence
    :return: a linked node structure representing the DNA sequence. Each character is a Node
    """
    if len( dna1 ) == 0:
        return None
    else:
        return LinkNode( dna1[ 0 ],convert_to_nodes( dna1[ 1: ] ) )

def is_match(dna1,dna2):
    """
    Checks to see if the two lists are matching with the exact same length and values
    :param dna1: dna sequence 1
    :param dna2: dna sequence 2
    :return: a boolean whter is is true or not
    """
    if dna1 is None and dna2 is None:
        return True
    elif dna1 is None or dna2 is None:
        return False
    elif dna1.value != dna2.value:
        return False
    else:
        return is_match(dna1.rest, dna2.rest)

def insertion(dna1,dna2,Index):
    """
    inserts the dna sequence into the other dna sequence
    :param dna1: dna sequence 1
    :param dna2: dna seqquence 2
    :param Index: index in which the insertion occurs
    :return: a new linked list sequence that represents the DNA strand after substitution mutation occurs
    """
    if Index==0:
        return linked_code.concatenate(dna2,dna1)
    elif dna1 is None:
        raise IndexError("Out of Bounds")
    else:
        return linked_code.LinkNode(dna1.value, insertion(dna1.rest,dna2, Index -1))

def is_pairing(dna, dna1):
    """
    this checks to see if the two values in the ists are a pair or not
    :param dna: the first DNA sequence
    :param dna1: the second DNA sequence
    :return: a boolean for whether it is a pair or not
    """
    if dna is None and dna1 is None:
        return True
    elif linked_code.length_rec(dna) == linked_code.length_rec(dna1):
        if dna.value == "A" and dna.value == "T":
            return is_pairing(dna.rest,dna1.rest)
        elif dna1.value == "A" and dna.value =="T":
            return is_pairing(dna.rest,dna1.rest)
        elif dna.value == "C" and dna1.value=="G":
            return is_pairing(dna.rest, dna1.rest)
        elif dna.value == "G" and dna1.value =="C":
            return is_pairing(dna.rest,dna1.rest)
        else:
            return False
    else:
        return False

def is_palindrome(dna):
    """
    This checks to see if the list is a palindrome or not.
    :param dna: the first dna sequence
    :return: whether it is true or not
    """
    if dna is None:
        return True
    elif linked_code.reverse_iter(dna).rest == dna.rest:
        return True
    else:
        return False

def substitution(dna1,Index, base):
    """
    THis substitutes a certain list into the dna stand calling it a mutation
    :param dna1: the first dna sequence
    :param Index: where the substituion should start
    :param base: the new base to be substituted at the specific index
    :return: the new linked list after the substitution occurs
    """
    if dna1 is None or Index<0:
        raise IndexError("Out of Bounds")
    else:
        linked_code.remove_at(Index,dna1)
        return linked_code.insert_at(Index,base, dna1)

def deletion(dna, Index, segment_size):
    """
    This deletes a certain amount of characters based on how big the segment size is.
    :param dna: the first dna sequence
    :param Index:the positon where it starts the deleting
    :param segment_size: the amount of how many characters should be deleted
    :return: the dna lsit of what is left
    """
    if segment_size==0:
        return dna
    elif segment_size> linked_code.length_rec(dna) or Index < 0:
        raise IndexError("Out of Bounds")
    else:
        return deletion(linked_code.remove_at(Index, dna),Index, segment_size - 1)

def duplication(dna, Index, segment_size):
    """
    This duplicates the code in the given segment size starting with the index and puts it after the original
    :param dna: the first dna sequence
    :param Index: where the duplication should start
    :param segment_size: how many characters should be duplicated
    :return: a new linked list after the duplication
    """
    #Could not get this to stop erroring.It looked like it was coming from the main function

    """
    if segment_size == 0:
        return dna
    elif segment_size > linked_code.length_rec(dna) and Index <= 0:
        raise IndexError("Out of Bounds")
    else:
        return duplication(dna.rest,linked_code.insert_at(Index,dna.value,dna),segment_size -1)
    """
