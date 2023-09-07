"""
A dataclass that represents "spots" on the skewer and functions that work
with it.

author: RITCS
author: Randy Dickersbach
"""

from dataclasses import dataclass
from typing import Union
from food import Food

@dataclass
class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a Food 'item',
        and a reference to the 'next' spot.
    """
    item: Food
    next: Union[None, 'KebabSpot']


def spot_create(item, next):
    """
    Create a new food item spot on the skewer
    :param item (Food): new food item
    :param next: next spot
    :return: new spot
    """

    KebabSpot.top = KebabSpot(item,  next)
    return KebabSpot.top



def spot_name(spot):
    """
    Return the name of the food item in this spot.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: food name
    """
    it = spot.item.name
    return it



def spot_size(spot):
    """
    Return the number of elements from this KebabSpot instance to the end
    of the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: the number of elements (int)
    """
    if spot is None:
        return 0
    else:
        return 1 + spot_size(spot.next)

def spot_has(spot, name):
    """
    Return whether there are is a food item from this spot to the end of
    the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :param name: the name (string) being searched for.
    :return True if any of the spots hold a Food item that equals the
    name, False otherwise.
    """
    if spot is None:
        return False
    elif spot.item.name == name:
        return True
    else:
        return spot_has(spot.next, name)

def spot_calories(spot):
    """
    gets the calories of an item
    :param spot: the current spot in the skewer
    :return: the calories as an int
    """
    calories = 0
    while spot is not None:
        calories += spot.item.calories
        spot = spot.next
    return calories

def spot_string_em(spot):
    """
    makes the stack into a normal stringed list
    :param: spot (KebabSpot): the spot on the skewer
    :return a list of strings of the stack
    """
    if spot is not None:
        spot_list = spot.item.name + "," +  spot_string_em(spot.next)
    else:
        return ""
    return spot_list

def spot_vegan(spot):
    """
    checks to see if the skewer is vegan or not
    :param spot: the spot
    :return: True or False
    """
    while spot is not None:
        if spot.item.veggie is False:
            return False
        spot = spot.next
    return True
