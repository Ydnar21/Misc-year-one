"""
file: node.py
language: python3
author: Bruce Herring
author: CS @ rit.edu
description:
   lecture code for a mutbale linked Node data type
"""

from dataclasses import dataclass
from typing import Any, Union

@dataclass
class Node:
    value: Any
    rest: Union[None, 'Node']
