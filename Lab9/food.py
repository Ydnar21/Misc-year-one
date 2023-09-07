"""
A module that represents the valid food types.

author: RITCS
author: << YOUR NAME HERE >>
"""
from dataclasses import dataclass
from typing import Union

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'mushroom', 'onion', 'pepper', 'tomato'}

# The set of vegetables
VEGGIES = {'onion', "pepper", 'tomato', 'mushroom'}   # TODO

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
    'mushroom' : 7,
}  # TODO

@dataclass(frozen=True)
class Food:
    name: str
    veggie : bool
    calories: int


def food_create(name):
    """
    Create a new food item.
    :param name: the name of the food
    :return: new Food object
    """
    if name in VEGGIES:
        food = True
    else:
        food = False
    food = Food(name, food, CALORIES[name])
    return food

